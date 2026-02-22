import speech_recognition as sr
import pyttsx3
from googletrans import Translator
engine = pyttsx3.init()
engine.setProperty('rate', 150)
translator = Translator()
languages = {
    "1": "fr", "2": "es", "3": "pt", "4": "nl",
    "5": "ga", "6": "de", "7": "hi", "8": "ur"
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
print("1.French 2.Spanish 3.Portuguese 4.Dutch")
print("5.Irish 6.German 7.Hindi 8.Urdu")
lang = languages.get(input("Choice (1-8): "), "hi")
text = listen()
if text:
    translated = translator.translate(text, dest=lang).text
    print("🌍 Translated:", translated)
    speak(translated)