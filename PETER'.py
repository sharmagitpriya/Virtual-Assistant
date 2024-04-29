import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

myName = 'Peter'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('Good Morning,Priya')
    elif hour>12 and hour<18:
        speak('Good Afternoon,Priya')
    else:
        speak('Good Evening,Priya')
    speak(f'I am {myName},How may I help you?')

def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....you.....')
        audio = r.listen(source)
    try:
        print('Recognizing...you....')
        query = r.recognize_google(audio,language='en=in')
        print('You said:', query)
    except Exception:
        print('say that again,please')
        return 'None'
    return query

def tellDay():

     

    # This function is for telling the

    # day of the week

    day = datetime.datetime.today().weekday() + 1

     

    #this line tells us about the number 

    # that will help us in telling the day

    Day_dict = {1: 'Monday', 2: 'Tuesday', 

                3: 'Wednesday', 4: 'Thursday', 

                5: 'Friday', 6: 'Saturday',

                7: 'Sunday'}

     

    if day in Day_dict.keys():

        day_of_the_week = Day_dict[day]

        print(day_of_the_week)

        speak("The day is " + day_of_the_week)
 
 

def tellTime():

     

    # This method will give the time

    time = str(datetime.datetime.now())

     

    # the time will be displayed like 

    # this "2020-06-05 17:50:14.582630"

    #nd then after slicing we can get time

    print(time)

    hour = time[11:13]

    min = time[14:16]

    speak( "The time is sir" + hour + "Hours and" + min + "Minutes")    


if __name__ =="__main__":
    wishme()
    while True:
        query = hearMe().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation error (when the search term has multiple possible meanings)
                print(f"There are multiple meanings for '{query}'. Please be more specific.")
                speak(f"There are multiple meanings for '{query}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found error (when the search term does not match any Wikipedia page)
                print(f"'{query}' does not match any Wikipedia page. Please try again.")
                speak(f"'{query}' does not match any Wikipedia page. Please try again.")
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open amazon' in query:
            webbrowser.open('www.amazon.com')
        elif 'open flipkart' in query:
            webbrowser.open('www.flipkart.com')
        elif 'show me your image' in query:
            os.startfile("C://Users//Priya//Pictures//Screenshot (10).png")
        elif 'open channel' in query:
            webbrowser.open('https://www.youtube.com/channel/UCtFOW7jJXChfFNoucRFqRmw')
        elif 'music from youtube' in query:
            os.startfile("https://www.youtube.com/shorts/rmure8rqgBY")
            speak('Playing Music....')
        elif 'open youtube' in query:
            os.startfile("www.youtube.com")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you,mam")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif 'tell me the day' in query:
            tellDay()
            continue
        elif "tell me the time" in query:
            tellTime()
            continue
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))


         

        # this will exit and terminate the program

        elif "bye" in query:

            speak("Thanks for giving your time have and have a  great day Priya")

            exit()
        #else:
           # search='https://www.google.com//search?q='+ query
            #webbrowser.open(search)


            
    
