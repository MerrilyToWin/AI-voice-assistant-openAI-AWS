import datetime
import os
import random
import time
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyaudio
import openai
import ctypes
import subprocess
import ecapture as ec
from config import apikey


#Voice engine initialization
engine = pyttsx3.init()


#Intro part
engine.say("Hello Sir I am Frank I am here for your assistance")
engine.runAndWait()


#Creating the folder to store the AI answers
folder= "C:/Prompt_Result"
if not os.path.exists(folder):
    os.makedirs(folder)
else:
    pass


#ChatBot
charStr = ""
def chat(command):
    global charStr
    openai.api_key = apikey

    charStr += f"User: {command}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=charStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    engine.say(response["choices"][0]["text"])
    engine.runAndWait()
    charStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



#Open AI prompt with solutions
def ai(command):
    #my apikey
    openai.api_key = apikey
    text = f"AI response for the prompt:{command}\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]

#Writing the prompt amswers in the file
    file=f"C:/Prompt_Result/{command}"
    with open(f"{file}.txt","w") as f:
        f.write(text)

#Viewing the prompt answer from the file
    with open(f"{file}.txt","r") as f:
        read_file=f.read()
    print(read_file)

    engine.say("Your File has been saved in the device sir.")
    engine.runAndWait()


# Function to perform various actions based on voice commands
def process_command(command):
    command = command.lower()

    #Creator
    if "who made you" in command or "who created you" in command:
        engine.say("I have been created by Merwin.")
        engine.runAndWait()

    # Default software in destop
    softwares = [["calculator", "calc.exe"], ["file manager", "explorer.exe"], ["notepad", "notepad.exe"],
                 ["paint", "mspaint.exe"], ["control panel", "control.exe"], ["task list", "tasklist.exe"],
                 ["command prompt", "cmd.exe"]]
    for software in softwares:
        if f"open {software[0]}" in command:
            engine.say(f"Opening {software[0]} Sir")
            engine.runAndWait()
            os.system(software[1])

    # Basic websites
    sites = ["youtube", "google", "wikipedia", "openai", "facebook", "instagram", "whatsapp"]
    for site in sites:
        if f"open {site}" in command:
            engine.say(f"Opening {site} Sir")
            engine.runAndWait()
            webbrowser.open(f"https://www.{site}.com")

    #Camera capture
    if "camera" in command or "take a photo" in command:
        ec.capture(0, "frame", "img.jpg")
        engine.say("Your photo has been saved in the device sir")
        engine.runAndWait()

    #Hibernation or sleep
    if "hibernate" in command or "sleep" in command:
        engine.say("Hibernating")
        engine.runAndWait()
        subprocess.call("shutdown / h")

    #Location
    if "where is" in command:
        command = command.replace("where is", "")
        location = command
        engine.say("User asked to Locate")
        engine.runAndWait()
        engine.say(location)
        engine.runAndWait()
        webbrowser.open("https://www.google.com/maps/place/" + location + "")

    #Dont listen
    if "dont listen" in command or "stop listening" in command:
        engine.say("I will not listen to you sir")
        engine.runAndWait()
        time.sleep(100)
        engine.say("I am back sir")
        engine.runAndWait()


    # Shut Down
    if 'lock window' in command or 'lock the screen' in command or 'lock the device' in command:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    if "bye" in command or "goodbye" in command or "exit" in command or "quit" in command:
        engine.say("Thank you for having me Sir,if you need any help call me")
        engine.runAndWait()
        exit()

    #Shutdown System
    if 'shutdown system' in command:
        engine.say("Hold On a Sec ! Your system is on its way to shut down")
        engine.runAndWait()
        subprocess.call('shutdown / p /f')

    #Reset chat
    if "frank" and "reset chat" in command:
        charStr = ""

    if command==None:
        engine.say("Sorry Sir, I did not catch the command")
        engine.runAndWait()

    else:
        chat(command)


#Looping
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language="en-in")
            print(command)
            if "frank" and  "using artificial intelligence" in command:
                ai(command)
            else:
                process_command(command)

        except sr.RequestError:
            engine.say("Sorry, I'm having trouble with my speech recognition. Please try again later.")
            engine.runAndWait()

