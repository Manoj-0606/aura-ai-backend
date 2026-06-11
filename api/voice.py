from fastapi import APIRouter

from voice.stt import listen
from agents.router_agent import route_query
from voice.neural_tts import speak

router = APIRouter()


@router.post("/voice-chat")
def voice_chat():

    user_text = listen()

    response = route_query(user_text)

    speak(response)

    return {
        "user": user_text,
        "response": response
    }