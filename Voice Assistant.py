import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import re
import datetime
import wikipedia
from bs4  import BeautifulSoup as soup
import urllib
import urllib2
from urllib2 import urlopen
import requests
import xml
#import subprocess
#import vlc

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audios = r.listen(source,timeout=1,phrase_time_limit=5)

        try:
            query = r.recognize_google(audios,language='en-in')
            speak(query)
            return query
        except Exception as e:
            print(e)
            print("Please said Again")
            return "None"



if __name__ == "__main__":
    speak("Hello World")
    query=takCommand()
    print(query)
    if 'open' in query:
        reg_ex=re.search('open (.+)',query)
        if reg_ex:
            domain=reg_ex.group(1)
            url="http//www"+domain+".com"
            wb.open(url)
            speak("The website is opened for you")
    if 'time' in query:
        print("Accepted")
        ctime=datetime.datetime.now()
        speak('Current time is %d hours %d minutes' % (ctime.hour, ctime.minute))
    if 'tell me about' in query:
        print("Search")
        reg_ex =re.search('tell me about(.*)',query)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                print(ny.content[:500].encode('utf-8'))
        except Exception as e:
                print(e)
    if 'today' in query:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:15]:
                speak(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
    # if 'online' in query:
    #     reg_ex = re.search('launch(.*)',query)
    #     if reg_ex:
    #         appname=reg_ex.group(1)
    #         appname1 =appname + ".exe"
    #         subprocess.Popen(["open", "-n", "/C:\Users\MDT/" + appname1], stdout=subprocess.PIPE)
    #         speak('I have launched the desired application')
        else:
            speak("Sorry ,I did not understand your command ") 