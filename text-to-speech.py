# text-to-speech.py
import pyttsx3 
engine = pyttsx3.init()
msg = input("Enter the message you want to convert to speech: ")
speed = int(input("Enter the speed of the speech (default is 200): ") or 200)
volume = float(input("Enter the volume of the speech (default is 1.0): ") or 1.0)

engine.setProperty('rate', speed)
engine.setProperty('volume', volume)
engine.say(msg)
engine.runAndWait()