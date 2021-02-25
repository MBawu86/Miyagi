import speech_recognition as sr 
import pyttsx3
import espeak
import ffmpeg
import pyaudio
import datetime
import wikipedia
import webbrowser
import time
import requests
import subprocess #proces sys command aka log-off etc
# import ecapture #camera
import playsound #audio feedback
import os #save/open files
# import wolframalpha #calc strings into formulas
from selenium import webdriver #controls browser operationms

output = ""
engine = pyttsx3.init()

# rate
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate',125)

# volume
volume = engine.getProperty('volume')
print(volume)

engine.setProperty('volume', 1.0)

# voice
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) 
engine.setProperty('voice', voices[1].id)

engine.say('Hello World')
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# saving voice to file
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
# def talk():
#   input = sr.Recognizer()
#   with sr.Microphone() as source:
#     audio = input.listen(source)
#     data = ""
#     try:
#       data = input.recognize_google(audio)
#       print("Your question is, " + data)
#     except sr.UnknownValueError:
#       respond("Speak clearly, kodomo.")
#     return data

# def respond(response):
#   global output
#   num = 0
#   print(output)
#   num += 1
#   response = pyttsx3(text = response, lang = "en") # pylint: disable=not-callable
#   file = str(num) + ".mp3"
#   response.save(file)

#   playsound.playsound(file, True)
#   os.remove(file)

# def response(input, output):
 
#   if __name__ == '__main__':
#     respond("Hello!  I am Mister Miyagi. You stay focused.")

#   while(1):
#     respond("What knowledge do you require, kodomo?")
#     text = talk().lower()

#     if text == 0:
#       talk()
# ###############################
#     if "goodbye" in str(text):
#       respond ("Remember, never put passion in front of principle, even if you win, you lose. Goodbye")
#       break
# #################################
#     if "wikipedia" in text:
#       respond('Searching Wikipedia')  
#       text = text.replace('wikipedia', '')
#       results = wikipedia.summary(text, sentences=5)
#       print(results)
#       respond(results)
# ###################################
#     elif 'time' in text:
#       strTime = datetime.datetime.now().strftime("%H:%M:%S")
#       respond(f'The time is {strTime} kodomo')
# ####################################
#     # elif 'find' in text:
#     #   question = talk()
#     #   text = text.replace('search', '')
#     #   webbrowser.open_new_tab(text)
#     #   time.sleep(5)

#     # elif 'calculate' or 'what is' in text:  
#     #   question = talk()
#     #   app_id = 'API key'
#     #   client = wolframalpha.Client(app_id)
#     #   res = client.query(question)
#     #   answer = next(res.results).text
#     #   respond("The answer is " + answer)

#     elif 'who are you' in text: 
#       respond("I am Mr. Miyagi")

# # responds application not available
#     # elif 'what can I do' in text:
#     #   respond('I can fetch information for you, perform mathematical calculation, open applications, get weather details.')
# ###################################
#     elif 'open google' in text:
#       webbrowser.open_new_tab('https://www.google.com')
#       respond('Google is now open')
#       time.sleep(5)
# ####################################
# # responds application not available
#     # elif 'open duck duck go' in text:
#     #   webbrowser.open_new_tab('https://www.duckduckgo.com')
#     #   respond ('Ninja web browser is now open')

#     # elif 'rumble' in text:
#     #   webbrowser.open_new_tab('https://www.rumble.com/')
#     #   respond ('You are ready to rumble')
#     #   time.sleep(5)

#     # elif "weather" in text:
#     #           respond("what is the city name")
#     #           zip_code=talk()
#     #           api_key="a0690ad0d685189ea33e3039e8b7b7a7"
#     #           base_url="https://api.openweathermap.org/data/2.5/weather?zip"
#     #           complete_url=base_url+"appid="+api_key+"&q="+zip_code
#     #           response = requests.get(complete_url)
#     #           x=response.json()
#     #           if x["cod"]!="404":
#     #               y=x["main"]
#     #               current_temperature = y["temp"]
#     #               current_humidiy = y["humidity"]
#     #               z = x["weather"]
#     #               weather_description = z[0]["description"]
#     #               respond(" Temperature is " +
#     #                     str(current_temperature) +
#     #                     "\n humidity in percentage is " +
#     #                     str(current_humidiy) +
#     #                     "\n description  " +
#     #                     str(weather_description))

#       # failed to parse time specification: /l            # 
#     # elif 'shut down' in text:
#     #   respond("Ok. Your system will shut down in 10 seconds")
#     #   subprocess.call(['shutdown', '/l'])

#     else:
#       respond('Application not available')

# response(input, output)