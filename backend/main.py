from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent

app = FastAPI(title="Unit Converter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConvertRequest(BaseModel):
    query: str


class ConvertResponse(BaseModel):
    result: str


@app.get("/")
def root():
    return {"status": "Unit Converter API is running"}


@app.post("/convert", response_model=ConvertResponse)
def convert(request: ConvertRequest):
    try:
        result = run_agent(request.query)
        return ConvertResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))