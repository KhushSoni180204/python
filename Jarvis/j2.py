import speech_recognition as sr
r=sr.Recognizer()
text=""
while text!="no":
    print("Please talk and Say No to Stop")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=4)
        print("Getting")
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))
        if text=="hello":
            print("how are you?")
        elif text=="how are you":
            print("I am fine")
        elif text=="hungry":
            print("let's eat something")
        elif text=="no":
            print("Bye")