import speech_recognition as sr
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    audio_data=r.record(source,duration=3)
    print("Recognizing....")
    text=r.recognize_google(audio_data)
    print(text)