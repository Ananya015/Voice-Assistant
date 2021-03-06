# VOICE ASSISTANT

# importing modules

# convert text-to-speech
import pyttsx3

# display current time
import datetime

# recognises speech
import speech_recognition as sr

# detect wekipidias
import wikipedia

# display web pages
import webbrowser

# interact with os
import os

# getting reference to pyttsx3.convert entered text to speech.
engine=pyttsx3.init('sapi5')

# pyttsx3 module support two voices i.e. 1st is of female and 2nd one is of male and it is supported by "sapi5"
voices=engine.getProperty('voices')

# selecting voice of female
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour <18:
        speak("Good afternoon!")
    else:
        speak("Good Evening")

    speak("I am jarvis, please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Say again please")
        return "None"
    return query


if __name__ == '__main__':
    # speak("hey ! welcome. This is Ananya")
    wishMe()


    while True:
         query=takeCommand().lower()


         if 'wikipedia' in query:
             speak("searching wikipedia...")
             query=query.replace("wikipedia","")
             results = wikipedia.summary(query , sentences=3)
             speak("according to wikipedia")
             print(results)
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open google' in query:
                webbrowser.open("google.com")

         elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

         elif 'play music' in query:
             music ="C:\\Users\\vinay kumar jain\\Desktop"
             songs =os.listdir(music)
             os.startfile(os.path.join(music, songs[0]))
         elif 'the time' in query:
             strtime=datetime.datetime.now().strftime("%H:%M:%S")
             speak("time is "+ strtime)
         elif 'open pycharm' in query:
             pych="C:\\Users\\vinay kumar jain\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-C\\ch-0\\202.6397.98\\bin\\pycharm64.exe"
             os.startfile(pych)
         elif 'stop' in query:
             speak("Thank you! for giving me a chance for serving you")
             break









