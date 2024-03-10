import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
r.energy_threshold = 4000
engine = pyttsx3.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone(1) as source:
        print("Speak now...")
        audio = r.listen(source,timeout=10)
    try:
        text = r.recognize_google(audio)
        return text;
    except:
        return None
    

while True:
    command = listen()

    if command is None:
        continue

    if "remind me" in command:
        print("hello")
        speak("What should I remind you about")
        reminder = listen()
        print(f"Sure, I'll remind you to {reminder} later.")
        

    elif "create a to-do list" in command:
        speak("What are the tasks you want to add to the to-do list?")
        tasks = []
        while True:
            task = listen()
            if "stop" in task:
                break
            tasks.append(task)
        speak("Here is your to-do list")
        for i, task in enumerate(tasks):
            speak(f"{i+1}, {task}")
        
    elif "search for" in command:
        query = command.replace("search for," "")
        speak (f"Here are the search results for {query},")


    elif "quit" in command:
        speak ("Goodbye!")
        break

    else:
        speak("I'm sorry, I didn't understand you. Could you say it again")