import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone(1) as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text;
    except:
        return None
    

while True:
    command = listen()

    if command is None:
        continue
    
    if "good morning" in command:
        speak("Good Morning! How are you doing?")
    
    elif "remind me" in command:
        speak("What should I remind you about")
        reminder = listen()
        speak(f"Sure, I'll remind you to {reminder} later.")
        

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