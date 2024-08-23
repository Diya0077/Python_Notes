import pyttsx3
engine = pyttsx3.init()
while(True):
    text = input("Enter what do you want me to speak: ")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    if(text=='q'):
        engine.say("Bye!")
        print("Bye!")
        exit()