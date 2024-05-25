import speech_recognition as sr
import subprocess
import pyautogui as py
import time

def voice():

    # Initialize recognizer
    r = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Listen for 5 seconds and create ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated")
        
        print("-------- !!  Order me Now !! --------")
        audio = r.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

app_list = [
    "Chrome",
    "Whatsapp",
    "Brave",
    "Spotify",
    "Telegram",
    "Visual Studio Code",
    "VLC Media Player"
]

def open_app(app_name):
    py.press('win')
    time.sleep(5)  # Changeable as per PC Capability and speed
    py.typewrite(app_name)
    time.sleep(2)
    py.press('enter')

print("< - - Available Apps to open- - >\n")
for i in app_list:
    print("  -> ", i)

print('\n\n')

choice = voice()

if ("chrome" in choice) or ("Chrome" in choice):
    subprocess.run("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", shell = True)
    

elif ("whatsapp" in choice) or ("Whatsapp" in choice):
    open_app('whatsapp')
    
elif ('Brave' in choice) or ('brave' in choice):
    open_app('brave')

elif ('Spotify' in choice) or ('spotify' in choice):
    open_app('spotify')

elif ('Telegram' in choice) or ('telegram' in choice):
    open_app('telegram')

elif ('Visual Studio Code' in choice) or ('vs code' in choice) or ('visual studio code' in choice) or ('visual studio' in choice):
    open_app('brave')

elif ('vlc' in choice) or ('VLC' in choice) or ('media player' in choice):
    open_app('vlc')

else:
    print("! - - Invalid choice - - !")