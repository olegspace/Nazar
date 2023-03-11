import pyautogui
import time
рб = input ("вы любите роблокс?")
if рб ==  "нет":
    print("я понимаю")
    pyautogui.moveTo(1259,10)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(25,1055)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(25,700)
    pyautogui.click()
    pyautogui.moveTo(25,620)
    time.sleep(2)
    pyautogui.click()
else:
    print("пока")