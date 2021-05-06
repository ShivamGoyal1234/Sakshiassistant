import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib
import wolframalpha 
import sys

client = wolframalpha.Client('Y9V4GQ-5XXW55WJ9T')
engine = pyttsx3.init('sapi5') # To take voice inbuilt voice        
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',200)


def speak(audio):
    print('Sakshi: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        print("Good Morning")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print("Good Evening")
        speak("Good Evening")

    
    speak('Hello Sir, I am your digital assistant Saakshi the Lady Jarvis!')
    speak('How may I help you?')

nam = "I am saakshi sir"
nam2 = "i am your assistant sir , I can do things for you "

def takeCommand():
        # it takes microphone input  from the user and return string output 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try :
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")   

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"    

        return query

def sendEmail(to, content):
    server = smtplib.SMTP('Smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email_id','password')
    server.sendmail('email_id', to, content)
    server.close()

name = True  
if __name__ == "__main__":
    wishme()

 
    
    while name:
        query = takeCommand().lower()

        if 'name' in query:
            print(nam)
            speak(nam)

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'who are you' in query:
            print(nam2)
            speak(nam2)       

        elif 'shut up' in query or 'quite' in query:
            print("i am sorry sir")
            speak("i am sorry sir")
            speak("Nice to work with you")
            exit()            

        elif 'how are you' in query or  "what\'s up" in query:
            stMgs = ['just doing my thing !', 'I am Fine','Nice!','i am nice and full of energy']
            speak(random.choice(stMgs))
        
       
        # Logic for Execution tasks based on query
        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query =query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            # print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("opening... please wait")
            webbrowser.open_new("youtube.com")
            speak("opened")

        elif 'open Google' in query or 'ok google' in query:
            speak("opening... please wait")
            webbrowser.open_new("google.com")
            speak("opened")

        elif 'open stackoverflow' in query:
            speak("opening... please wait")
            webbrowser.open_new("stackoverflow.com") 
            speak("opened")  

        elif 'open facebook' in query:
            speak("opening... please wait")
            webbrowser.open_new("facebook.com")
            speak("opened")   
    

        elif 'play music' in query:
            music_dir = 'E:\\swati'
            songs = os.listdir(music_dir)
            random_gen = random.randint(0, len(songs)- 1)
            os.startfile(os.path.join(music_dir, songs[random_gen]))  # calling that file randomly
            print("okay, Here is your music enjoy")
            speak("okay, Here is your music enjoy")
        


        elif 'the time' in query or 'the current time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time - {strtime}\n")
            speak(f"Sir, the time is {strtime}")
           

        elif 'open code' in query:
            codepath ="C:\\Users\\swati\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

       

        elif 'send email' in query:
            try:
                speak("To Whom You want to send sir ? Please enter a email")
                to = input("please enter a email: ")
                speak("what should i write in Email :")
                content = takeCommand()
                speak("Email has been sent")
                sendEmail(to, content)
                
               

            except Exception as e:
                print(e)
                speak("sorry, I am not able to send this email ")
        
        
        elif 'exit' in query or 'bye' in query or 'shutdown' in query:
            speak("quitting sir. Thanks For your time")
            name = False
            
        
        # else: 
        #     query = query

        elif 'weather' in query or  '+' in query or '-' in query or '*' in query or '=' in query or '%' in query: 
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('My Searching says')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    # results = wikipedia.summary(query, sentences=1)
                    # speak('Got it.')
                    # speak('WIKIPEDIA says - ')
                    # speak(results)
                    pass

            except:
                pass   
    