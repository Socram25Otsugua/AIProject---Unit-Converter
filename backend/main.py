from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    # TODO: wire up agent in next commit
    return ConvertResponse(result=f"Received: {request.query} (agent not connected yet)")