import asyncio
import edge_tts
import os


async def speak(text):

    filename = "aura_voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )

    await communicate.save(filename)

    os.system(f'start "" "{filename}"')


if __name__ == "__main__":

    asyncio.run(
        speak(
            "Hello Manoj. I am Aura AI. Nice to meet you."
        )
    )