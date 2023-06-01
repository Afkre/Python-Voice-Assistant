import speech_recognition as spr

r=spr.Recognizer()

with spr.Microphone() as source:
    audio  = r.listen(source)
    voice    = r.recognize_google(audio , language='tr-TR')
    print(voice)