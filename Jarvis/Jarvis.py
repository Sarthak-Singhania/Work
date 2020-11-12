import speech_recognition as sr
from time import ctime
from gtts import gTTS
import os
import time
def speak(audioString):
    tts=gTTS(text=audioString,lang='en')
    tts.save('speech.mp3')
    os.system('mpg321 speech.mp3')
def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio=r.listen(source)
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
def jarvis(data):
    if 'how are you' in data:
        speak('I am  fine')
    if 'what time is it' in data:
        speak(ctime())
    if 'where is' in data:
        data=data.split(' ')
        location=data[2]
        speak('Hold on Sarthak, I will show you where '+ location + 'is.')
        os.system('chromium-browser https://www.google.com/maps/place/'+location+'/&amp;')
time.sleep(2)
speak('Hello Sarthak, what can I do for you?')
while 1:
    data=recordAudio()
    jarvis(data)