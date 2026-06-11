import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

            print("You:", text)

            return text

        except sr.WaitTimeoutError:

            return ""

        except sr.UnknownValueError:

            print("Could not understand audio")

            return ""

        except sr.RequestError:

            print("Speech API unavailable")

            return ""

        except KeyboardInterrupt:

            print("Stopping AURA...")

            return "exit"

        except Exception as e:

            print("Error:", e)

            return ""