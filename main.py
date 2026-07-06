from ast import Break
import queue
from re import T
import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import pywhatkit
import subprocess
import os





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
        print("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
        print("Good Afternoon sir")

    else:
        speak("Good Evening sir")
        print("Good Evening sir")

    speak("I am EDITH , How can i help you")
    print("I am EDITH , How can i help you")

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        

        if   'youtube search' in query:
                     speak('Opening YouTube sir.')
                     print('Opening YouTube sir')
                     query=query.replace("youtube search","")
                     web='https://www.youtube.com/results?search_query=' + query
                     webbrowser.open(web)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"sir, the time is{strTime}")
            print(strTime)

        elif 'play' in query:
         song = query.replace('play', '')
         speak('playing ' + song)
         pywhatkit.playonyt(song)

        elif 'join my class' in query:
            speak('Joining Your Class Sir.')
            print('Joining Your Class Sir.')
            webbrowser.open_new_tab(url='https://meet.google.com/xei-xhuy-zcg?authuser=2')

        elif 'open classroom' in query:
            speak('Opening Google Class room sir.')
            print('Opening Google Class room sir.')
            webbrowser.open_new_tab(url='https://classroom.google.com/u/2/c/MTE4MzA0NzY2ODE4')

        elif 'fine' in query:
            speak('ok sir glad to hear that sir.')
            print('ok sir glad to hear that sir.')

        elif 'how are you' in query:
            speak('i am fine sir. What about you sir ?')
            print('i am fine sir.')

        elif 'search' in query:
            speak('searching result sir.')
            query= query.replace("search","")
            find=query
            pywhatkit.search(find)
            speak(find)

        elif 'open chrome' in query:
            speak('Opening Chrome sir.')
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')


        elif 'close chrome' in query:
            speak('Closing chrome.')
            os.system("taskkill /f /im chrome.exe")


        elif 'open vs code' in query:
            speak('opening vs code.')
            os.startfile("C:\\Users\\A Roshan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'close vs code ' in query:
            speak('closing vs code sir.')
            os.system("taskkill /f /im Code.exe")
    

        elif 'open blender' in query:
            speak('Opening Blender sir.')
            print('Opening Blender sir.')
            os.startfile('C:\\Program Files\\Blender Foundation\\Blender 3.0\\blender.exe')



        elif 'do animation' in query:
            speak('Sure sir . Shall i open Blender sir ?')
            print('Sure sir . Shall i open Blender sir ?')


        elif 'open whatsapp' in query:
            speak('Opening whatsapp sir .')
            print('Opening whatsapp sir .')
            os.startfile('C:\\ProgramData\\A Roshan\\WhatsApp\\WhatsApp.exe')



        elif 'close whatsapp' in query:
            speak('Closing whatsapp sir.')
            print('Closing whatsapp sir.')
            os.system("taskkill /f /im whatsapp.exe")



        elif 'who are you'in query:
            speak('i am edith. your ai .')
            print('i am edith. your ai .')

        elif 'take break' in query:
            speak("Ok Sir , You can call me anytime.")
            print("Ok Sir , You can call me anytime.")
            break

        elif 'to chicken ' in query:
            speak('Go and die .')
            print('Go and die .')


        elif 'enable volume' in query:
            speak('Activating Volume Gestures .')
            print('Activating Volume Gestures .')
            os.startfile('C:\\Users\\A Roshan\\PycharmProjects\\Project EDITH\\F --- Volume G.py')

        elif 'disable volume' in query:
            speak('Disabled Volume Gestures')
            print('Disabled Volume Gestures')
            os.system("taskkill /f /im py.exe")
        
