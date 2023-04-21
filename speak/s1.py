import pyttsx3
import speech_recognition as sr
r=sr.Recognizer()
engine = pyttsx3.init()
text=""
while text!="no":
    print("Please talk and Say No to Stop")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=4)
        print("Getting")
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))
        if text=="hello":
            engine.say("how are you?")
            engine.runAndWait()
        elif text=="I am fine":
            engine.say("good")
            engine.runAndWait()
        elif text=="hungry":
            engine.say("let's eat something")
            engine.runAndWait()
        elif text=="no":
            engine.say("Bye")
            engine.runAndWait()