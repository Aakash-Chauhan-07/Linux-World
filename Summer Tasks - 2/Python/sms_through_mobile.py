"""
Connect to your mobile and send sms from your mobile using python.

    Pre - Configurations:

        --> Connect your phone with Phone link app in your pc.
        
        --> Download --link to windows-- app from play store.

        --> Now, Complete the pairing process

"""

import pyautogui as py
import time

phone = input("Enter the phone number or name (If number exist in contact list) of the person you want to send message: ")
msg = input("\nType your message here: ")

py.press('win')
time.sleep(3)

py.typewrite("Phone Link")
time.sleep(5)

py.press('enter')
time.sleep(8)  # Depend on performance -- Please link the phone link with mobile before running the script

message = py.locateOnScreen("message.png")
time.sleep(2)

py.click(message)
time.sleep(2)

compose = py.locateOnScreen("compose.png")
time.sleep(2)

py.click(compose)
time.sleep(2)

py.typewrite(phone)
time.sleep(2)

py.press('enter')
time.sleep(2)

send = py.locateOnScreen('send.png')
time.sleep(3)

py.click(send)
time.sleep(3)
py.click(send)
time.sleep(2)

py.typewrite(msg)
time.sleep(1)

py.press('enter')


print("Your message has been sent Successfully.")