from fastapi import APIRouter

from models.chat import ChatRequest, ChatResponse
from agents.router_agent import route_query

from memory.chat_memory import add_message
from services.profile_service import get_profile
from memory.progress_memory import get_workouts

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Save user message
    add_message("user", request.message)

    # Process query
    response = route_query(request.message)

    # Save assistant response
    add_message("assistant", response)

    return ChatResponse(response=response)


@router.get("/profile")
def profile():

    return get_profile()

@router.get("/workouts")
def workouts():

    return {
        "workouts": get_workouts()
    }