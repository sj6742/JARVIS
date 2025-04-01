#_____________________________________________________________________________________________________________
'''
TO OPERATE JARVIS OR TEST A JARVIS COMMAND, USE THESE COMMANDS

1) FOR JOKES:- " JARVIS, TELL ME A JOKE."
2) FOR OPEN WEBPAGE:- "JARVIS, OPEN YOUTUBE."
3) FOR NEWS:- "JARVIS, NEWS HEADLINES"
4) FOR MUSIC:- "JARVIS, PLAY SHAPE OF YOU"

'''     
#_____________________________________________________________________________________________________________

import speech_recognition as sr  # Helps the program listen to you and convert your speech into text
import webbrowser #THIS LIB IS USED FOR OPEN URLs IN A WEB BROWSER
import pyttsx3  # Converts text into speech, so the assistant can talk back to you.
import musicLibrary #THIS CONTAIN MUSIC LINK LIB. FOR PLAY MUSIC LINK  
import random #USED FOR RANDOMLY SELECTING A JOKE FROM A LIST
import requests #USED TO FETCH DATA FROM A NEWS API

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text): #speak(text):-  USED pyttx3 engine for convert the text passed into speach....
    engine.say(text)
    engine.runAndWait() #processes the speach queue and wait up for it to finish

# FOR JOKES TELL JARVIS (JARVIS TELL ME A JOKE)
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? (Because they make up everything!)",
        "Why did the scarecrow win an award? (Because he was outstanding in his field!)",
        "Why don’t skeletons fight each other? (They don’t have the guts!)",
        "What do you call fake spaghetti? (An impasta!)"
    ]
    joke = random.choice(jokes)
    print(f"Telling joke: {joke}")  
    speak(joke)

# FETCH NEWS HEADLINES

def get_news():
    API_KEY = "06a8072720634a79b110ccaeedca4f76"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get("articles", [])


# FOR NEWS YOU NEED TO TELL JARVIS ('NEWS HEADLINES')
        if articles:
            speak("Here are the top news headlines.")
            for i, article in enumerate(articles[:5]):
                headline = article.get("title", "No title available")
                print(f"News {i+1}: {headline}")
                speak(headline)
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("There was an error fetching the news.")

# TO OPEN WEBSITE YOU NEED TO TELL JARVIS TO (JARVIS OPEN 'YOUTUBE')
def processCommand(c):  #THIS COMMAND IS RESPONSIBLE FOR PROCESSING USER`S COMMANDS...
    print(f"Recognized command: {c}")  
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")   
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")  
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://wikipedia.com")
    elif "tell me a joke" in c.lower():
        tell_joke()
    elif "tell me the news" in c.lower() or "news headlines" in c.lower():
        get_news()
    
    # FOR PLAYING MUSIC
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song, "")
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song in your library.")
    else:
        speak("Website not recognized.")          

if __name__ == '__main__': #WHEN THE PROGRAM STARTS IT ANNOUNCES THAT IT IS INITIALIZING JARVIS
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(f"Wake word detected: {word}")  
            if word.lower() == "jarvis":
                speak("Yes?")
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)    
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")  
                    processCommand(command)
        
        except Exception as e:
            print(f"Error: {e}")
