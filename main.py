import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT import music
from News import *
import randfacts
from jokes import *



engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',160)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello there, I am your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am having a good day")
speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in wikipedia".format(infor))
    print("Searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want me to play which video?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on youtube".format(vid))
    print("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure, here are some latest news that I will read for you.")
    speak("Sure, here are some latest news that I will read for you.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])


elif "fact" or "facts" in text2:
    speak("Sure,")
    x = randfacts.get_fact()
    print(x)
    speak("Did u know that," + x)

elif "joke" in text2 or "jokes" in text2:
    setup, punchline = joke()
    speak("Sure, get ready for some chuckles")
    if setup != "No joke found":
        print(setup)
        speak(setup)
    if punchline:
        print(punchline)
        speak(punchline)
    elif setup == "No joke found":
        print("Sorry, couldn't find any joke at the moment.")
        speak("Sorry, couldn't find any joke at the moment.")



