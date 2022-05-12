import imp
from importlib.resources import path
import pyttsx3
import speech_recognition as sr #input speech module
import datetime
import wikipedia 
import webbrowser
import os #for playing music and other stuff
import random
from playsound import playsound


engine = pyttsx3.init('sapi5') # sapi5 is a api used by microsoft in speech recognition refer MS site 
voices = engine.getProperty('voices') # getProperty is a inbuilt function which is in pyttsx3 which we are accessing by creating engine as a object
                                        # getProperty just shows number of voices available for example male and female 

engine.setProperty('voices', voices[0].id) # now by using setProperty we are setting the voice which we want'
#print(voices[1].id)

def speak(audio): # this is the speak function
    engine.say(audio) # audio is a string which will be spoken by engine.say() function
    engine.runAndWait()

def wishMe(): # Whishing function
    hour = int(datetime.datetime.now().hour) # It will give us hours from 0 to 24 which is stored in var 'hour'   

    if hour>=0 and hour<12:          # Wishing Logic
        speak('Good Morning Rishav')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Rishav')
    else:
        speak('Good Evening')
    
    reply = takeCommand().lower()
    if "Good morning jarvis" or "Good afternoon jarvis" or "Good evening jarvis" in reply:
        speak("Hello sir, Iam Jarvis. How may I help you")


def takeCommand(): # it takes microphone input from user and returns string output
    
    
    r = sr.Recognizer() # setting recoginizer module in var 'r' by using recognizer class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # time taken to show result after user done speaking (also you can click on threshold while holding ctrl to see all thresholds)
        audio = r.listen(source) # Putting user speech in 'audio' var by using recognizer module

    try:  # checking for possibles errors using try        
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # just changing user audio to text 
        print(f"User said: {query}\n")
    
    except Exception as e:  # if the above try block did not execute then we go in this exection block
        #print(e)
        print("Say that again please...")
        flag = 1
        return None
    return query

 
wishMe()
if 1: 
    query = takeCommand().lower()
    if 'wikipedia' in query:
        print("Searching Wikipedia....")
        query = query.replace("wikipedia", "") # replaces wikipedia with null for the next iteration
        results = wikipedia.summary(query, sentences=5) # store wikipedia summary in result by using summary function
        speak("According to wikipedia")
        print(results)
        #speak(results)

    elif "youtube" in query:
        webbrowser.open("youtube.com")
    
    elif "google" in query:
        webbrowser.open("google.com")

    elif "instagram" in query:
        webbrowser.open("instagram.com")

    elif "play music" or "music" or "songs" in query:
        
        path = "D:\\Songs"     
        songs = os.listdir(path) # listdir() will list all music present in music_dir in songs 
        playMusic = random.choice(songs) # choice() storing random music in 'playMusic' 
        os.startfile(playMusic)
        # Note = your py files must in Songs folder in order to play music 
        

    elif "the time" in query:                               
        strTime = datetime.datetime.now().strftime("%H:%M:%S") # return time in string format and store in 'strTime'
        speak(f"Sir the time is {strTime}") 

    


                                 

