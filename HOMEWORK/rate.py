import pyttsx3
engine = pyttsx3.init()
while(True):
    text = input("Enter what you want me to speak: ")
    engine.say(text)
    engine.runAndWait()
    if(text == 'q'):
        print("Bye Bye my Friend! I will miss you ")
        engine.say("Bye Bye my Friend! I will miss you ")
        exit()
