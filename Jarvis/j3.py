import speech_recognition as lol
r=lol.Recognizer()
text=""
while text!="no":
    with lol.Microphone() as source:
        audio_data=r.record(source,duration=5)
        print("Recognizing....")
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))
        if text=="india"or text=="India":
            print("Capital of India is New Delhi")
        elif text=="usa"or text=="america"or text=="USA"or text=="America":
            print("Capital of USA is Washington")
        elif text=="japan"or text=="Japan":
            print("Capital of Japan is Tokyo")
        elif text=="russia"or text=="Russia":
            print("Capital of Russia is Moscow")
        elif text=="exit":
            print("Bye")
            break