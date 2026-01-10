import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
engine.setProperty('rate', 150)
translator = Translator()

languages = {
    "1": "hi", "2": "ta", "3": "te", "4": "bn",
    "5": "mr", "6": "gu", "7": "ml", "8": "pa"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("🎙️  Speak in English...")
        audio = r.listen(src)
    try:
        text = r.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except:
        print("❌ Could not understand")
        return ""

print("Choose language:")
print("1.Hindi 2.Tamil 3.Telugu 4.Bengali")
print("5.Marathi 6.Gujarati 7.Malayalam 8.Punjabi")

lang = languages.get(input("Choice (1-8): "), "hi")

text = listen()
if text:
    translated = translator.translate(text, dest=lang).text
    print("🌍 Translated:", translated)
    speak(translated)



