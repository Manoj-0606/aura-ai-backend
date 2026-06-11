from fastapi import FastAPI
from pydantic import BaseModel

from agents.router_agent import route_query

app = FastAPI(title="AURA AI")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "AURA AI Running"}

@app.post("/chat")
def chat(request: QueryRequest):

    response = route_query(request.query)

    return {
        "query": request.query,
        "response": response
    }