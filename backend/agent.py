import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain.prompts import PromptTemplate

from tools import (
    kg_to_lbs, lbs_to_kg,
    gallons_to_liters, liters_to_gallons,
    meters_to_feet, feet_to_meters,
    fahrenheit_to_celsius, celsius_to_fahrenheit,
    mph_to_kmh, kmh_to_mph,
    convert_currency,
)
from prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# --- Define LangChain Tools ---

def _currency_wrapper(input: str) -> str:
    """Parse 'amount FROM_CURRENCY TO_CURRENCY' and call convert_currency."""
    try:
        parts = input.strip().split()
        amount = float(parts[0])
        from_cur = parts[1]
        to_cur = parts[2]
        return convert_currency(amount, from_cur, to_cur)
    except Exception:
        return "Invalid input. Use format: '100 USD EUR'"


TOOLS = [
    Tool(name="kg_to_lbs", func=lambda x: kg_to_lbs(float(x)),
         description="Convert kilograms to pounds. Input: a number (e.g. '10')."),
    Tool(name="lbs_to_kg", func=lambda x: lbs_to_kg(float(x)),
         description="Convert pounds to kilograms. Input: a number (e.g. '22')."),
    Tool(name="gallons_to_liters", func=lambda x: gallons_to_liters(float(x)),
         description="Convert gallons to liters. Input: a number (e.g. '5')."),
    Tool(name="liters_to_gallons", func=lambda x: liters_to_gallons(float(x)),
         description="Convert liters to gallons. Input: a number (e.g. '20')."),
    Tool(name="meters_to_feet", func=lambda x: meters_to_feet(float(x)),
         description="Convert meters to feet. Input: a number (e.g. '3')."),
    Tool(name="feet_to_meters", func=lambda x: feet_to_meters(float(x)),
         description="Convert feet to meters. Input: a number (e.g. '9')."),
    Tool(name="fahrenheit_to_celsius", func=lambda x: fahrenheit_to_celsius(float(x)),
         description="Convert Fahrenheit to Celsius. Input: a number (e.g. '98.6')."),
    Tool(name="celsius_to_fahrenheit", func=lambda x: celsius_to_fahrenheit(float(x)),
         description="Convert Celsius to Fahrenheit. Input: a number (e.g. '37')."),
    Tool(name="mph_to_kmh", func=lambda x: mph_to_kmh(float(x)),
         description="Convert miles per hour to kilometers per hour. Input: a number (e.g. '60')."),
    Tool(name="kmh_to_mph", func=lambda x: kmh_to_mph(float(x)),
         description="Convert kilometers per hour to miles per hour. Input: a number (e.g. '100')."),
    Tool(name="convert_currency", func=_currency_wrapper,
         description="Convert between currencies. Input: 'amount FROM TO' (e.g. '100 USD EUR')."),
]

# --- ReAct prompt template ---

REACT_TEMPLATE = """You are a unit conversion assistant.

{system}

You have access to these tools:
{tools}

Use this format:
Question: the input question you must answer
Thought: think about what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Observation as needed)
Thought: I now know the final answer
Final Answer: the final answer to the original question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    partial_variables={"system": SYSTEM_PROMPT},
    template=REACT_TEMPLATE,
)

# --- Build agent ---

llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL, temperature=0)
agent = create_react_agent(llm=llm, tools=TOOLS, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=TOOLS,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=6,
)


def run_agent(query: str) -> str:
    """Run the agent with a user query and return the result string."""
    user_prompt = build_user_prompt(query)
    response = agent_executor.invoke({"input": user_prompt})
    return response.get("output", "No response from agent.")