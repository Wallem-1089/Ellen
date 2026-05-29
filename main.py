import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
from plyer import notification, battery, screenshot, brightness, bluetooth, wifi

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hi Am Ellen')
engine.runAndWait()

# Aptoide
'''
add the reminder feature(upgrade it to deal with today, tomorrow, and time statements), get microphones that serve as 
speakers, so you the audio access from anywhere, add other features, use this to make others with apis, use this to
set brightness, to check battery, take screenshots, on bluetooth and wifi.'''


def talk(text):
    engine.say(text)
    engine.runAndWait()


while True:
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ellen' in command:
                command = command.replace('ellen', '')
                print(command)
                if 'play' in command or 'video' in command:
                    song = command.replace('play', '')
                    talk('playing' + song)
                    pywhatkit.playonyt(song)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    talk('Current time is ' + time)
                elif 'who is' in command:
                    search = command.replace('who is', '')
                    info = wikipedia.summary(search, 1)
                    print(info)
                    talk(info)
                elif 'set' and 'reminder' in command:
                    reminder = ''
                    if __name__ == '__main__':
                        while True:
                            notification.notify(
                                title="Alert",
                                message="Take a break! It has been an hour",
                                timeout=10
                            )
                            time.sleep(10)
                else:
                    ''' use the a google search scraper here '''
            else:
                talk('please say the command again')
    except:
        pass
