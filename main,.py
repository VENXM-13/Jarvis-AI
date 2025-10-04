import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi= "fd7ab9d6686647028eabf4011f09ea47"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text=text, lang='en', tld='co.uk')
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(command):
    client = OpenAI(
    api_key="Add Your Open AI Key here",)

    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. I need short and concise Answers "},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open wikipedia" in c.lower():
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")
    elif "open gmail" in c.lower():
        speak("Opening G-mail")
        webbrowser.open("https://www.gmail.com")
    elif "open gitHub" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "open reddit" in c.lower():
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
    elif "open spotify" in c.lower():
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
    elif "open amazon" in c.lower():
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
    elif c.lower().startswith("play"):
        speak("Playing Music..")
        song= c.lower().split(" ")[1]
        link= musiclib.music[song]
        webbrowser.open(link) 
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={newsapi}")
        if r.status_code == 200:
            data =r.json()

            articles= data.get("articles",[])
            speak("Here are the Top news Headlines..")

            for article in articles:
                speak(article["title"])

    else:
        output= aiProcess(c)
        speak(output)
        

    
    

if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            # recognize speech using Google Speech Recognition
            print("recognizing...")
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Master..")
                # Listen to command
                with sr.Microphone() as source:
                    print("Jarvis Listening....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
        except Exception as e:
            print("Google error; {0}".format(e))
