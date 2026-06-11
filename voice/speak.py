import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)   # Zira Female
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

engine.say("Hello Manoj. I am Aura AI.")
engine.runAndWait()