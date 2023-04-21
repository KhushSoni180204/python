import speech_recognition as lol
r=lol.Recognizer()
n1=0
n2=0
text=""
print("Speak 1 number")
with lol.Microphone() as source:
    audio_data=r.record(source,duration=5)
    print("Recognizing....")
    n1=r.recognize_google(audio_data)
    print(n1,"--",len(n1))
    a=int(n1)

print("Speak 2 number")
with lol.Microphone() as source:
    audio_data=r.record(source,duration=5)
    print("Recognizing....")
    n2=r.recognize_google(audio_data)
    print(n2,"--",len(n2))
    b=int(n2)

print("Speak operation")
with lol.Microphone() as source:
    audio_data=r.record(source,duration=5)
    print("Recognizing....")
    text=r.recognize_google(audio_data)
    print(text,"--",len(text))
    if text=="Addition"or text=="addition":
        print("Add = ",a+b)
    elif text=="Division"or text=="division":
        print("Div = ",a/b)
    elif text=="Subtraction"or text=="subtraction":
        print("Sub = ",a-b)
    elif text=="Multiplication"or text=="multiplication":
        print("Mul = ",a*b)
    else:
        print("Sorry invalid input")