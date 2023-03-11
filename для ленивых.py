import keyboard
import pyautogui
import time

def komanda(bukva):
    global num
    for step in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        pyautogui.press(bukva)

def komandaa():
    global num
    for step in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        pyautogui.press("a")
def komandaw():
    global num
    for step in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        pyautogui.press("w")
buk = input("какую букву писать?")
keyboard.add_hotkey("", komanda(buk))       
#keyboard.add_hotkey("a", komandaa)
#keyboard.add_hotkey("w", komandaw)