import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import os
import yfinance as yf 
import pyjokes
import wikipedia

# listen to the microsphone and return the audio as text using google
def transformMic():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        personSaid =r.listen(source)
        # Avoiding Error
        try:
            print('I am listing')
            text = r.recognize_google(personSaid, language = "en")
            return text
        except sr.UnknownValueError:
            print('Sorry I do not understand')
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"
transformMic()

# def speaking(message):
#     engine = pyttsx3.init()
#     engine.say(message)
#     engine.runAndWait()

# speaking('Hello World,I am Grogu')

# see what is installed
# currently David
engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
# changing voice 
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello World,I am Grogu')
engine.runAndWait()
def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Returns the weekday name
def getDay():
    day = datetime.date.today()
    # print(day)
    weekday = day.weekday()
    # print(weekday)
    mapping = {
        0: 'Monday',1: 'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is{mapping[weekday]}')
    except:
        pass


# Gets the current time 
def getTime():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    # strftime("%I:%M:%S") formats string time
    print(time)
    try:
        speaking(f" {time[1]} o çlock and {time[3:5]} minutes")
    except:
        pass


# Greeting function at start up 
def greeting():
    speaking(''' 
    Hi, My name is Grogu. 
    I am your personal assistant.
    How may I help you today?
    ''')


# Main funcation heart of Grogu.Takes queries and returns anwers
def heartOfBot():
    # first thing
    greeting()
    start = True
    while(start):
        q = transformMic().lower()
# starts youtube
        if 'start youtube' in q:
            speaking('Start youtube.Just a second')
            webbrowser.open('https://www.youtube.com')
            continue
# starts google
        elif 'start google' in q:
            speaking('Opening browser')
            webbrowser.open('https://www.google.com')
            continue
# Gives day
        elif 'what day is it' in q:
            getDay()
            continue
# gives time
        elif 'what is the time' in q:
            getTime()
            continue
       
# search wikipedia
        elif 'from wikipedia' in q:
            speaking('checking wikipedia')
            q = q.result('wikipedia','')
            result = wikipedia.summary(q,sentences = 2)
            speaking('found on wikipedia')
            speaking(result)
            continue
# provides its name
        elif 'your name' in q:
            speaking('I am Grogu. Your Virtual assistance')
            continue

        elif 'search web' in q:
            pywhatkit.search(q)
            speaking('this is what i have found')
            continue
# play a song on youtube
        elif 'play' in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
# telling jokes 
        elif 'joke' in q:
            speaking(pyjokes.get_joke())
            continue
# stock price
        elif 'stock price' in q:
            search = q.split('of')[-1].strip()
            lookup ={'apple': 'AAPL','amazon':'AMZN','google':'GOOGL'}
            try:
                stock = lookup[search]
                stock=yf.Ticker(stock)
                currentprice = stock.info['regularMarketPrice']
                speaking(f'found it! the stock price of {search} is {currentprice}')
                continue
            except:
                speaking(f'I have no data for {search}')
                continue
# Close Grogu
        elif 'goodbye' in q:
            speaking('Okay bye')
            break
heartOfBot()
