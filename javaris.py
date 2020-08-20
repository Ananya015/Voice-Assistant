import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


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
        query = r.recognize_google(audio, language="en-US")
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




