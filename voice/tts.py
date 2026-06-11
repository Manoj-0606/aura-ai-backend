import asyncio
import edge_tts
import uuid


def speak(text):

    filename = f"response_{uuid.uuid4().hex}.mp3"

    async def generate():

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-JennyNeural"
        )

        await communicate.save(filename)

    asyncio.run(generate())

    return filename