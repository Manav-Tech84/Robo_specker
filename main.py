
import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeck 1.0 create by me")
    # initialize the text-to-speech engine
    while True:
        engine = pyttsx3.init()
        text_to_speech = input("Enter what you want, I speck for you: ")
        if  text_to_speech =="q":
           break
        engine.say(text_to_speech)
        engine.runAndWait()
