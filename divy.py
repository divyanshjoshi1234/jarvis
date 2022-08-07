from sys import implementation, path
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

no = random.randint(1,6)
x=1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")

    elif hour>=12 and hour<15:
        speak("Good afternoon  sir!")
    
    elif hour>=15 and hour<19:
        speak("Good evening sir!")

    else:
        speak("Good night  sir!")

    speak(" I am divya  sir . ram 4gb . memory 1 terabite .. i can do any thig for you sir . i hope you are fine and happy. you can ask any thing . please tell me how may i help you")

    

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("any thing sir....")
       

        print("listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing .....")
        query = r.recognize_google(audio,language='en.in')
        print(f"user said :{query}\n")

    except Exception as e:
        print(e)
        
        speak( "say it again sir .....")
        return "None"
    return query


if __name__ == '__main__':
     speak(" divya is here sir")
     wishme()
     while (x==1):
      
     
         query= takecommand().lower()
         # you can modefy this according to you and your computer
         # put address according to your computer

         if 'wikipedia' in query:
             speak('searching wikipedia.....')
             query = query.replace("wikipedia" , "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results) 

         elif  'hello' in query:
             speak("hello sir")
         elif  'open youtube' in query:
             speak("opening youtube for you sir")
             webbrowser.open("youtube.com")
         elif  'open google' in query:
             speak("opening google for you sir")
             webbrowser.open("google.com")
         elif  'open mail' in query:
             speak("opening mail for you sir")
             webbrowser.open("mail.com")    
         elif 'play music' in query:
             speak("playing music for you sir") 
             music_dir='F:\\music'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[no]))

         elif 'open image' in query:
             speak("opning images  for you sir") 
             image_dir='C:\\Users\\DIVYANSH\\Music\\New folder (2)'
             images = os.listdir(image_dir)
             print(images)
             os.startfile(os.path.join(image_dir, images[no]))

         elif 'play movie' in query:
             speak("play movies  for you sir") 
             movie_dir='G:\\movies\\Hindi'
             movies = os.listdir(movie_dir)
             print(movies)
             os.startfile(os.path.join(movie_dir, movies[no]))

         elif 'the time'in query:
             strTime= datetime.datetime.now().strftime("%H:%M:%S")
             speak(f" sir the time is {strTime}")
        
         elif 'open code' in query:
             speak("opening VS code for you sir")
             codePath = "C:\\Users\\DIVYANSH\\Desktop\\VSCodeUserSetup-x64-1.53.2.exe"
             os.startfile(codePath)

         elif 'open pc' in query:
             speak("opening pycharm for you sir")
             code = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
             os.startfile(code)

         elif 'open GTA' in query:
             speak("opening gta for you sir")
             gtaPath = "C:\\Interesting Hack Games\\Grand Thief Auto Vice City\\gta-vc.exe"
             os.startfile(gtaPath)

         elif 'bye' in query:
             speak(" by sir.... stoping my program  sir...... have a nice day sir . if you need help you can restart me any time sir . i will we there for you sir ........ by sir ..." )
             x=2
        
        
         elif 'stop' in query:
             speak(" by sir.... stoping my program  sir...... have a nice day sir . if you need help you can restart me any time sir . i will we there for you sir ........ by sir ..." )
             x=2
         elif 'no thanks' in query:
             speak(" by sir.... stoping my program  sir...... have a nice day sir . if you need help you can restart me any time sir . i will we there for you sir ........ by sir ..." )
             x=2


        
         elif 'you are good' in query:
             speak("thankyou sir .. its my plasure if you think so .. i will try my best for you ...")

        
         elif 'you are useless' in query:
             speak("sorry sir.. if i have done any mistake .. i will try to improve me .. sorry sir................")

        
         elif 'i am bored' in query:
                 speak("you can watch movie sir")
                 speak("play movies  for you sir") 
                 movie_dir='G:\\movies\\Hindi'
                 movies = os.listdir(movie_dir)
                 print(movies)
                 os.startfile(os.path.join(movie_dir, movies[no]))

         elif 'date with me' in query:
            
             speak("sorry sir i am in relationship with your wifi .... and he asked me first ...")

         elif 'i love you' in query:
             speak("really... i love you too .... but i am in relationship with my work.")

# we cn add mare elif to fullfill our reqirment
  
        