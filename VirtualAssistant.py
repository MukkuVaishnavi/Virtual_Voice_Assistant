# Project1
# Import the following Libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
# Support of Voice
engine = pyttsx3.init('sapi5') #Speech Recognisation API
voices= engine.getProperty('voices') #To hear the response of the sysytem;by default we have 5 voices;in this case we are using 0 index voice
# Using this for loop to see the different voices present in our device
for i in voices:
    print(i)
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)
# Making a function to make the system speak the given audio
# Making use of inbuilt speaker
# We are converting Text to Audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Testing our function
# speak('Hello')
# Based on the current date and time I want my assistant to wish me
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring Buddy!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Buddy!")
    else:
        speak("Good Evening Buddy!")
    speak("I am Kas, How may I come to your service today?")
# Testing our function
# wishMe()
# Making a Function to take our Command from our inbuilt Microphone
# It takes Audio as input and returns String output
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        # print(f"User said:{query}\n")
        print("User said: ",query)
    except Exception as e :
        print("Sorry,Could you please say that again...")
        return "None"
    return query
# Testing our function
# TakeCommand()
# Functions for performing various actions
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pythonproject0323@gmail.com','Python@1234')
    server.sendmail('pythonproject0323@gmail.com',to,content)
    server.close()
# Testing the function
# sendEmail('mukkuvaishnavi122003@gmail.com','Hey...')
if __name__ =="__main__":
    wishMe()
    while True:
        query= TakeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            # results=wikipedia.search(query,results=2)
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = r"C:\Users\Mukku Vaishnavi\Desktop\Winter Training\Songs"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play' in query:
            music_dir = r"C:\Users\Mukku Vaishnavi\Desktop\Winter Training\Songs"
            songs = os.listdir(music_dir)
            query= query.lower().replace("play ","")  
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[songs.index(f"{query}.mp3")]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time right now is {strTime}")
        elif 'open code' in query:
            codePath =r"C:\Users\Mukku Vaishnavi\Desktop\Winter Training\Project"
            os.startfile(codePath)
        elif 'email to ' in query:
            try:
                speak("Okay! What is the concering Email ID?")
                to = TakeCommand()
                speak("What should I say?")
                content = TakeCommand()
                to = ""    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am Sorry Buddy.I am not able to send this email.Please Try again Later") 
        elif 'Thank You' in query:
            speak("No Problem Buddy! Alaways there for you")
            break