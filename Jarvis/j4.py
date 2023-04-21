import speech_recognition as lol
r=lol.Recognizer()
text=""
while text!="no":
    print("Speak any number")
    with lol.Microphone() as source:
        audio_data=r.record(source,duration=5)
        print("Recognizing....")
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))
        if text.isnumeric():
            a=int(text)
            for i in range(1,11):
                print(a,"*",i,"=",a*i)
        else:
            print("Sorry wrong input")