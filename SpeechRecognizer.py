import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything: ")
    audio=r.listen(source)
    try:
        text=r.recogniz_google(audio)
        print("you said: {}".format(text))
    except:
        print("sorry could not recognise your voice")
