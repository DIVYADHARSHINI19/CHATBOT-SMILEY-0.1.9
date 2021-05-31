import os
from time import sleep
import gtts as gt
from playsound import playsound
import speech_recognition as sr
from datetime import datetime

### TEXT TO SPEECH (MACHINE) TAMIL

def tamilTextToSpeech(speak):
    tts = gt.gTTS(text=speak, lang='ta')
    tts.save("Tamil-Audio.mp3")
    playsound("Tamil-Audio.mp3")
    sleep(1)
    os.remove("Tamil-Audio.mp3")


def tamilSpeechToText():
    text = ""
    global WhatUSpoke
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something in Tamil")
        playsound("beep.mp3")
        audio = r.listen(source)
        playsound("pika.mp3")
        try:
            text = r.recognize_google(audio, language="ta-IN")
            print("What you spoke :", text)

        except Exception:
            print("recognition failed")

        return text


def tamilspeak():
    while True:
        now = datetime.now()
        outputt = tamilSpeechToText()

        if "உன் பேர் என்ன" in outputt:
            tamilTextToSpeech("என் பெயர் நிலா")
            print("என் பெயர் நிலா")
        elif "ஹாய்" in outputt:
            tamilTextToSpeech("ஹலோ, நீ் எப்டி இருக்க")
            print("ஹலோ, நீ் எப்டி இருக்க")
        elif "வணக்கம்" in outputt:
            tamilTextToSpeech("வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்")
            print("வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்")
        elif "சாப்டியா" in outputt:
            tamilTextToSpeech("எனக்கு உணவு எதுவும் இல்லை")
            print("எனக்கு உணவு எதுவும் இல்லை")
        elif "என்ன பண்ற" in outputt:
            tamilTextToSpeech("உங்களுடன் பேசிக் கொண்டிருக்கிறேன்")
            print("உங்களுடன் பேசிக் கொண்டிருக்கிறேன்")
        elif "எப்படி இருக்க" in outputt:
            tamilTextToSpeech("நான் நல்லா இருக்கேன்")
            print("நான் நல்லா இருக்கேன்")
        elif "ஆங்கிலம்" in outputt:
            break
        else:
            tamilTextToSpeech(outputt)