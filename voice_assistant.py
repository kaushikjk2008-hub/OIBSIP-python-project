import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

command = input("Say Hello: ")

if command.lower() == "hello":
    speak("Hello Aarti, how can I help you?")
else:
    speak("Sorry, I did not understand.")
