import keyboard

num = 0
def komanda():
    global num
    num = num + 1
    if num == 10:
        print("всё!")
        num = 0
keyboard.add_hotkey("win+alt", komanda)