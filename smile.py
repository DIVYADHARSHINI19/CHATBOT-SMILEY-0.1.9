import pyaudio
from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime
import random
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import calendar


# TEXT TO SPEECH

def Speak(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    # Use female voice
    engine.setProperty('voice', voice_id)
    engine.runAndWait()

# SPEECH TO TEXT (user)

def Talk():
    text = ""
    r = sr.Recognizer()
    print("Speak Now !!")
    playsound("start.mp3")
    with sr.Microphone() as source:
        audio = r.listen(source)
        playsound("end.mp3")
        try:
            text = r.recognize_google(audio)
            print("you said: " + text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            Speak("Google Speech Recognition could not understand audio")
            Talk()

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0} ".format(e))
            Speak("Could not request results from Google Speech Recognition service; {0} ".format(e))
            Talk()

        return text

## PLAYING AUDIO

def play_audio(song_name):
    song_name = song_name.replace(' ', '%20')
    url = 'https://gaana.com/search/{}'.format(song_name)
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    links = soup.findAll('a', {'class': 'rt_arw'})
    webbrowser.open(links[0]['href'])

### CONTENT FOR SPEAKING

greetings = ["Hello", "Hi", "Hola", "Hey there", "Yo", "Yes, Smiley here.", "Hey"]
commonTalks = {"hi": "hey",
               "who are you" : "I am smiley, your personal assistant",
               "how are you": "I am fine , and you?",
               "what are you doing": "I am Communicating with you",
               "what's new": " COVID-19 third wave",
               "what is new": " COVID-19 third wave",
               "who created you": "I was made by Divya dharshini",
               "did you eat": "Usually i don't eat, but i like cotton candy",
               "did you had your lunch": "Actually, i don't eat",
               "did you eat your breakfast": "Actually, i don't eat",
               "did you had your dinner": "Actually, i don't eat",
               "which food do you like": "The thing is i like everything, but especially i like biriyani",
               "your favourite food": "The thing is i like everything, but especially i like biriyani",
               "which colour do you like": "I like colours that are bright and contrast",
               "which cartoon do you like": "I love 90's cartoon like Tom and jerry, shinchan, Doraemon and power rangers",
               "your age": " As i born in 2021, you can calculate my age,right?",
               "what is your name": "I am waiting for this moment to say my name. My name is Smiley",
               "your favourite movie": " i love to watch mysterious movies",
               "what's up": "Just waiting for you",
               }
Good = {"good morning": "Happy morning 😊, did you sleep well ?",
        "good afternoon": "Good afternoon 🍔, Did you had your lunch?",
        "good evening": "Gud eve, how you are doing? ",
        "good night": "Good night 😴, sweet dreams"
}

thank = ["welcome!","you are welcome","My pleasure","Don't mention"]
youtube = ["YouTube","videos","play movie","play videos","open YouTube","play video"]
gaana = ["play some music","play songs","songs","gana","play music"]


#### STARTING THE CHATBOT

print('Starting the chatbot...')
password = Talk()
if password == "hello smiley":
    print("Yes, Smiley here")
    print('Chatbot started!')
    Speak("Yes, Smiley here")

    ####  RUNNING IT SPONTANEOUSLY
    while True:
        output = Talk()
        now = datetime.now()
        x = datetime.now()
        # x.strftime("%X")
        # time_wish = str(x).split(":")
        # gud = time_wish[0]
        # value = int(gud)

        # time, date, day, month, year subjects
        if "time" in output:
            current_time = now.strftime("%I:%M %p")
            print("Current Time is ", current_time)
            Speak("Current time is " + current_time)
        elif "date" in output:
            todate = datetime.today()
            current_date = todate.strftime("%B %d, %Y")
            print("Today's date is ", current_date)
            Speak("Today's date is " + current_date)
        elif "day" in output:
            today = datetime.today()
            current_day = today.strftime("%A")
            print("Today is", current_day)
            Speak("Today is " + current_day)
        elif "month" in output:
            month = datetime.now()
            current_month = month.strftime("%B")
            print("This month is " + current_month)
            Speak("This month is " + current_month)
        elif "year" in output:
            year = datetime.now()
            current_year = year.strftime("%Y")
            print("This year is " + current_year)
            Speak("This year is " + current_year)
        elif "thank" in output:
            thanks = random.choice(thank)
            print(thanks)
            Speak(thanks)
        elif "made" in output:
            print("I was made by Divya dharshini")
            Speak("I was made by dheevya dharsheene")
        elif "calculator" in output:
            Speak("The calendar for this year is 2021")
            print(calendar.calendar(2021, 2, 1, 6))

        elif output in youtube:
            webbrowser.open('www.youtube.com')
            Talk()
        elif "Google" in output:
            webbrowser.open('www.google.com')
            Talk()
        elif output in gaana:
            song_type = input('Do you like to listen music, then please type "audio"')
            Speak("If you want to listen music please type audio")
            song = input('Enter Song Name : ')
            Speak("Please Enter song name")
            song_type = song_type.lower()
            if 'audio' in song_type:
                play_audio(song)
            Talk()
        elif output in commonTalks.keys():
            print(commonTalks[output])
            Speak(commonTalks[output])
        elif output in Good.keys():
            print(Good[output])
            Speak(Good[output])
        elif output[0:6] == "define":
            search_query = output[7:]
            try:
                data = wikipedia.summary(search_query)
            except:
                data = "Too many word occurances. Try being more specific!!"
            print(data)
            Speak(data)
        elif "hello" in output:
            helo = random.choice(greetings)
            print(helo)
            Speak(helo)
        # elif "good" in output:
        #     if value > 00 and value < 12:
        #         print("Good morning")
        #     elif value >= 12 and value < 16:
        #         print("Good Afternoon")
        #     elif value >= 16 and value < 19:
        #         print("Good Evening")
        #     elif value >= 19 and value <= 23:
        #         print("Good Night")
        #     else:
        #         print("nothing")
        else:
            print("Sorry. Could not understand you.")
            Speak('Sorry. Could not understand you.')


else:
    print("Wrong password")
    Speak("Wrong password")
    exit()













