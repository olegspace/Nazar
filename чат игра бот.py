import pyautogui
import time
print("привет!")
name = input("какое у тебя имя?")
print(name + " хммммм хорошее имя")
time.sleep(1)
answer = input("давай поиграем?")
if answer == "давай" or answer == "да":
    print("первая игра это угодай число")
    time.sleep(1)
    print("правило игры: угадай число от 1 до 100")
    time.sleep(1)
    playone = input("готов?")
    if playone == "да":
        print("давай начнём!")
        
        while(True):
            playtwo = int(input(":"))
            if playtwo == 11:
                print("угадал")
                break;
            elif playtwo  > 11:
                print("поменше")
            elif playtwo  < 11:
                print("побольше")
            else:
                playtwo = input(": ")
        print("ты угадал")
        time.sleep(1)
        how  = input("раз ты выиграл давай тогда во 2 игру?")
        if how == "давай" :
            print("хорошо")
            time.sleep(1)
            print("это игра сложная ведь теперь тебе нужно найти файл чтобы узнать пароль!")
            while(True):
                poisk = int(input(": "))
                if poisk == 99788:
                    print("правильно!")
                    break;
            print("хммм а ты не ребёнок чтобы так играть?")
            time.sleep(2)
            print("ладно давай начнём третию игру!")
            time.sleep(1)
            print("правило игры!")
            time.sleep(1)
            print("повторяй цвета который будет писать бот!")
            time.sleep(1)
            print("но если ты неправильно ответишь то тебя съест баба карина")
            time.sleep(1)
            print("только не трогай мышь когда будут песать цвета!")
            time.sleep(1)
            print("начнём!")
            time.sleep(0.5)
            print("красный")
            time.sleep(0.5)
            print("зелёный")
            time.sleep(0.5)
            print("синий")
            time.sleep(0.5)
            print("розовый")
            time.sleep(0.5)
            pyautogui.moveTo(317, 667)
            pyautogui.moveTo(317, 667)
            pyautogui.moveTo(317, 667)
            pyautogui.moveTo(317, 667)
            pyautogui.moveTo(317, 667)
            pyautogui.click(button = 'right')
            pyautogui.moveTo(349, 633)
            pyautogui.click()
            pyautogui.click(button = 'right')
            color = input("красный\n")
            if color == "красный":
                colortwo = input("зелёный\n")
                if colortwo == "зелёный":
                    colorthree = input("синий\n")
                    if colorthree == "синий":
                        colorfor = input("розовый\n")
                        if colorfor == "розовый":
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            print("ха")
                            time.sleep(1)
                            print("ты думал что всё легко?")
                            time.sleep(1)
                            print("ведь я знаю что ты читер")
                            time.sleep(1)
                            print("вот тебе накозание")
                            pyautogui.moveTo(25, 1055)
                            time.sleep(0.5)
                            pyautogui.click()
                            pyautogui.moveTo(25, 689)
                            time.sleep(0.5)
                            pyautogui.click()
                            pyautogui.moveTo(25, 615)
                            time.sleep(0.5)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.click()
                else:
                    print("неправильно попробуй ещё раз")
        else:
            print("жаль")
    else:
        print("жаль")
else:
    print("жаль")
