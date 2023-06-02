import speech_recognition as spr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
#from playsound import playsound
import random
import os
from pydub import AudioSegment
from pydub.playback import play


r=spr.Recognizer()

def record(ask=False):    
    with spr.Microphone() as source:
        if ask:
            speak(ask)
        audio  = r.listen(source)
        voice= ''
        try:
            voice   = r.recognize_google(audio , language='de-DE')
        except spr.UnknownValueError:
            speak('Ich habe es nicht verstanden.')
        except spr.RequestError:
            speak('System funktioniert nicht.')            
        return voice

def response(voice):
    if 'wie gehr es dir':
        speak('Mir geht es gut, und wie geht es Ihnen?')
    if 'Wie viel Uhr ist es?':
        speak(datetime.now().strftime('5H:5M:%S'))
    if   'such im Internet' in voice:
        search = record ('Was wollen Sie im Internet suchen?') 
        url =  'http://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'gefunden')
    if 'okey' in voice:
        speak('Wenn Sie weitere Fragen haben, stehe ich Ihnen gerne zur Verfügung.')
        exit()

"""
def speak(string):
    antwort = gTTS(string, lang='de')
    rand = random.randint(1,5000)
    file = 'audio-'+str(rand)+'.mp3'
    antwort.save(file)
    playsound(file)
    os.remove(file)
"""
def speak(string):
    antwort = gTTS(string, lang='de')
    rand = random.randint(1, 5000)
    file = 'audio-' + str(rand) + '.mp3'
    antwort.save(file)

    audio = AudioSegment.from_mp3(file)
    play(audio)

    os.remove(file)    

speak('Wie kann ich Ihnen helfen?')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)