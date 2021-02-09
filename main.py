import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import time
import requests
import subprocess #proces sys command aka log-off etc
import ecapture #camera
import playsound #audio feedback
from gtts import gTTS #text2speech 
import os #save/open files
import wolframalpha #calc strings into formulas
from selenium import webdriver #controls browser operationms

output = ""

def talk():
  input = sr.Recognizer()
  with sr.Microphone as source:
    audio = input.listen(source)
    data = ""
    try:
      data = input.recognize_google(audio)
      print("Your question is, " + data)
    except sr.UnknownValueError:
      print("Speak clearly, kodomo.")
    return data

def respond(response):
  global output
  num = 0
  print(output)
  num += 1
  response = gTTS(text = response, lang = "en") # pylint: disable=not-callable
  file = str(num) + ".mp3"
  response.save(file)

  playsound.playsound(file, True)
  os.remove(file)



def response(input, output):
 
  if __name__ == '__main__':
    respond("Hello!  I am Mister Miyagi. You stay focused.")

  while(1):
    output("What knowledge do you require, kodomo?")
    text = talk().lower()

    if text == 0:
      continue

    if "goodbye" in str(text):
      output ("Remember, never put passion in front of principle, even if you win, you lose. Goodbye")
      break

    if "wikipedia" in text:
      respond('Searching Wikipedia')  
      text = text.replace('wikipedia', '')
      results = wikipedia.summary(text, sentences=5)
      print(results)
      respond(results)

    elif 'time' in text:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      output(f'The time is {strTime} kodomo')

    elif 'search' in text:
      text = text.replace('search', '')
      webbrowser.open_new_tab(text)
      time.sleep(5)

    elif 'calculate' or 'what is' in text:  
      question = talk()
      app_id = 'API key'
      client = wolframalpha.Client(app_id)
      res = client.query(question)
      answer = next(res.results).text
      output("The answer is " + answer)

    elif 'who are you' in text: 
      output =("I am Mr. Miyagi")

    elif 'what can I do' in text:
      output  ('I can fetch information for you, perform mathematical calculation, take photos or screenshots for you, open applicaitons, get weather details.')

    elif 'open google' in text:
      webbrowser.open_new_tab('https://www.google.com')
      output('Google is now open')
      time.sleep(5)

    elif 'open duck duck go' in text:
      webbrowser.open_new_tab('https://www.duckduckgo.com')
      output ('Ninja web browser is now open')

    elif 'rumble' in text:
      webbrowser.open_new_tab('https://rumble.com/')
      output ('You are ready to rumble')
      time.sleep(5)

    elif "weather" in text:
              output("what is the city name")
              zip_code=talk()
              api_key="a0690ad0d685189ea33e3039e8b7b7a7"
              base_url="https://api.openweathermap.org/data/2.5/weather?zip"
              complete_url=base_url+"appid="+api_key+"&q="+zip_code
              response = requests.get(complete_url)
              x=response.json()
              if x["cod"]!="404":
                  y=x["main"]
                  current_temperature = y["temp"]
                  current_humidiy = y["humidity"]
                  z = x["weather"]
                  weather_description = z[0]["description"]
                  output(" Temperature is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                  
    elif 'shut down' in text:
      output("Ok. your system will shut down in 10 seconds")
      subprocess.call(['shutdown', '/l'])

    else:
      output('Application not available')

response(input, output)
