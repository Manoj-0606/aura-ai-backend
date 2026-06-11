from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.voice import router as voice_router
from api.tts import router as tts_router

app = FastAPI(
    title="AURA AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat_router)
app.include_router(voice_router)
app.include_router(tts_router)

@app.get("/")
def root():
    return {
        "message": "AURA AI Backend Running"
    }