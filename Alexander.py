import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(" I am Alexander, how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising......")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)
    except Exception as e:
        print("say again......")
        return "none"
    return query
if __name__== "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)
        elif 'open mail' in query:
            webbrowser.open("gmail.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir ='C:\\Users\\hp\\Music\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam , the time is {strTime}")
        elif 'open visual studio code' in query:
            path="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'joke' in query:
            bummer=pyjokes.get_joke()
            print(bummer)
            speak(bummer)   
        elif 'email to neelam' in query:
            try:
                speak("what should i say")
                content =takeCommand()
                to ="neelnisk@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry mam , can't send the email at the moment")

            



    
