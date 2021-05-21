import pyaudio
from selenium import webdriver
import os
import gtts as gt
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import speech_recognition as sr
from translate import Translator
from datetime import datetime
import pyjokes
import random
import pyttsx3
import wikipedia
import pywhatkit as kit
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
            print("Smiley can't hear clearly, try again")
            Speak("Smiley can't hear clearly, try again")
            Talk()

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0} ".format(e))
            Speak("Could not request results from Google Speech Recognition service; {0} ".format(e))
            Talk()
        print("hey there : " + text)
        return text

## TRANSLATE TO TAMIL

def tamilTextToSpeech(TamilText):

    tts = gt.gTTS(text=TamilText, lang='ta')
    tts.save("Tamil-Audio.mp3")
    # os.system("Tamil-Audio.mp3")
    playsound("Tamil-Audio.mp3")


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

thank = ["welcome!","You are most welcome","My pleasure","Don't mention"]


def run():
    while True:
        output = Talk()
        print("dfaefhiuwheg  iuwaehfieghf", output)
        now = datetime.now()

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

        elif "calendar" in output:
            Speak("The calendar for this year is 2021")  ## CALENDAR
            print(calendar.calendar(2021, 2, 1, 6))

        elif output[0:9] == "translate":
            tamil = output[10:]
            try:
                translator = Translator(to_lang="ta-IN")  ## TAMIL TRANSLATION
                translation = translator.translate(tamil)
                print(translation)
                tamilTextToSpeech(translation)
            except Exception:
                print("Sorry unable to translate")

        elif "jokes" in output:  ## PY JOKES
            jokes = pyjokes.get_joke()
            print(jokes)
            Speak(jokes)

        elif "Google" in output:
            webbrowser.open('www.google.com')  ## OPENING GOOGLE
            Talk()

        elif 'video' in output:
            print("You Reached the END!!")
            Talk()
            # Speak('playing ' + output)  ## PLAYING YOUTUBE VIDEO
            # kit.playonyt(output)
            # Talk()

        elif "music" in output:
            Speak("If you want to listen music please type audio")
            song_type = input('Do you like to listen music, then please type "audio"')
            Speak(" Enter song name")
            song = input('Enter Song Name : ')
            song_type = song_type.lower()
            if 'audio' in song_type:  ## FOR PLAYING SONGS
                try:
                    play_audio(song)
                except:
                    print("Sorry unable to search")
                    pass
            Talk()

        elif output in commonTalks.keys():  ## SOME COMMON TALKS
            print(commonTalks[output])
            Speak(commonTalks[output])

        elif output in Good.keys():  ## GOOD MORNING MESSAGES
            print(Good[output])
            Speak(Good[output])

        elif output[0:6] == "define":  ## WIKIPEDIA
            search_query = output[7:]
            try:
                data = wikipedia.summary(search_query, 1)
            except:
                data = "Too many word occurances. Try being more specific!!"
            print(data)
            Speak(data)
        elif "message now" in output:
            phone = input("Enter phone number: ")
            message = input("Enter message ")
            try:
                kit.sendwhatmsg_instantly(f'+91{phone}', message, 10)
            except Exception:
                print("Sorry, Message not sent")
                Speak("Sorry, Message not sent")
                Talk()

        elif "message later" in output:
            phone = input("Enter phone number: ")
            message = input("Enter message ")
            hour = int(input("Enter which hour do you want to send msg "))
            minute = int(input("Enter which min you want to send msg"))
            try:
                kit.sendwhatmsg(f'+91{phone}', message, hour, minute, 30)
            except Exception:
                print("Sorry, Message not sent")
                Speak("Sorry, Message not sent")
                Talk()

        elif "hello" in output:  ## GREETINGS LIKE HELLO
            helo = random.choice(greetings)
            print(helo)
            Speak(helo)

        else:
            if output != "":
                pass
                try:
                    print("Searching...", output)
                    Speak("Searching..")
                    kit.search(output)
                except Exception:
                    pass
            Talk()

#### STARTING THE CHATBOT

print('Starting the chatbot...')
password = Talk()
print(password)
if password == "hello smiley":
    print("Yes, Smiley here")
    print('Chatbot started!')
    Speak("Yes, Smiley here")
    run()

## checking the password if wrong

else :
    print("wrong password")
    Speak("wrong password")
    Talk()


