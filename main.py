import speech_recognition as sr
import win32com.client
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want to speak it out by computer")
#     s = input()
#     speaker.Speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__=='__main__':
    print('Hello Jai')
    while True:
        print('Listening...')
        text = takeCommand()
        if "Open Youtube".lower() in text.lower():
            speaker.Speak("Opening Youtube")
            webbrowser.open("https://youtube.com")
        # speaker.Speak(text)

    
