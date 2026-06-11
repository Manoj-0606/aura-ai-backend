from fastapi import APIRouter
from fastapi.responses import FileResponse

from voice.tts import speak

router = APIRouter()


@router.post("/speak")
def text_to_speech(data: dict):

    text = data.get("text", "")

    audio_file = speak(text)

    return FileResponse(
        audio_file,
        media_type="audio/mpeg",
        filename=audio_file
    )