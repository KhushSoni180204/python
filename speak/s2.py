import pyttsx3
import speech_recognition as lol
r=lol.Recognizer()
e=pyttsx3.init()
text=""
while text!="no":
    with lol.Microphone() as source:
        audio_data=r.record(source,duration=5)
        e.say("Recognizing....")
        e.runAndWait()
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))
        if text=="india"or text=="India":
            e.say("Capital of India is New Delhi")
            e.runAndWait()
        elif text=="usa"or text=="america"or text=="USA"or text=="America":
            e.say("Capital of USA is Washington")
            e.runAndWait()
        elif text=="japan"or text=="Japan":
            e.say("Capital of Japan is Tokyo")
            e.runAndWait()
        elif text=="russia"or text=="Russia":
            e.say("Capital of Russia is Moscow")
            e.runAndWait()
        elif text=="exit":
            e.say("Bye")
            e.runAndWait()
            break