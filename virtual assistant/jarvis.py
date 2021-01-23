import pyttsx3#text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)#to find voices

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Hello, I'm Jarvis. Please tell me how can i help you?")
#it takes microphone input from user and return output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1#if any pause is their it will hold for 1 min
        audio = r.listen(source)
    
    try:
        print("Regonizing...")
        query = r.recognize_google(audio,language = 'en-in')#to recognize by google
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Please,Say that again...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

#logic for executing task based on query
        if 'wikipedia' in query:
             speak('Searching wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=3)
             speak("According to wikipedia")
             print(results)
             speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'open whatsapp web' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open site' in query:
            webbrowser.open("login.gitam.edu")

        elif 'send email' in query:
            try:
                speak(" What should i say?")
                content = takeCommand()
                to = "sender-email@gmail.com"
                sendEmail(to,content)
                speak("Email has sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        elif 'quit' in query:
            quit()

            
        