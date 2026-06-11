from voice.stt import listen
from agents.router_agent import route_query
from voice.tts import speak


def run_voice_chat():

    print("\n=== AURA Voice Assistant Started ===")
    print("Say 'exit' to stop.\n")

    while True:

        print("\n🎤 Listening...")

        user_text = listen()

        if not user_text:
            continue

        print("\nUSER:")
        print(user_text)

        if user_text.lower() in [
            "exit",
            "quit",
            "goodbye aura"
        ]:
            speak("Goodbye Manoj. Have a great day.")
            break

        response = route_query(user_text)

        print("\nAURA:")
        print(response)

        speak(response)


if __name__ == "__main__":
    run_voice_chat()