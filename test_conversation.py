from voice.stt import listen
from voice.tts import speak
from agents.router_agent import route_query

print("AURA Voice Assistant Started")

while True:

    user_text = listen()

    if not user_text:
        continue

    if user_text.lower() in ["exit", "quit", "stop", "goodbye"]:

        print("Goodbye Manoj!")

        speak("Goodbye Manoj!")

        break

    try:

        response = route_query(user_text)

        print("\nAURA:", response)

        speak(response)

    except Exception as e:

        print("AURA Error:", e)

        speak("Sorry, something went wrong.")