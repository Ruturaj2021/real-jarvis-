
import code
from email.mime import audio
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print ("Initializing Jarvis")
MASTER="Ruturaj"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
   engine.say(text)
   engine.runAndWait()
speak("initializing jarvis......")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour <12 :
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)


    else:
        speak("Good Evening"+MASTER)
        speak ("I am Jarvis. how may I help you?"+ MASTER)
    
    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0)  as source: 
        print("Listening...")
        
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
       print("Say that again please")
       query=None
    return query

speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower():

    speak ('Searching wikipedia....')
    query = query.replace("wikipedia","")
    results= wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.open("google.com")

elif 'play arijit singh song' in query.lower():
    webbrowser.open("https://www.youtube.com/watch?v=iyrvB5tl7ts")

elif 'open multiplayer car racing game' in query.lower():
    webbrowser.open("http://127.0.0.1:5500/multiplayer-car-racing-game-10-SA-main/index.html")

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is{strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'open chrome' in query.lower():
    codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(codePath)

elif 'open white hat junior' in query.lower():
    webbrowser.open("https://code.whitehatjr.com/s/dashboard")

elif 'open calculator' in query.lower():
    codePath = "C:\\Users\\DELL\\OneDrive\\Desktop\\Calculator.lnk"
    os.startfile(codePath)

elif 'open calendar' in query.lower():
    codePath = "C:\Users\DELL\OneDrive\Desktop\Calendar.lnk"
    os.startfile(codePath)

elif 'open excel' in query.lower():
    codePath = "C:\Users\DELL\OneDrive\Desktop\Excel.lnk"
    os.startfile(codePath)

elif 'open github' in query.lower():
    webbrowser.open("https://github.com/")