import string, random

















items_shop = {"хлеб": 7,
              "вода": 5,
              "чипсы": 14,
              "сок": 16,
              "ключ": 21,
              "ключ?": 78,
              "...": 999,
              "семечки": 5}

items_attack = {"бита": 15,
                "крепкая бита": 50,
                "некрепкая бита": 10}
cto = "нечто"
nepr = 0
#if cto in items_shop.keys():
    #print("Такое еcть")
#else:
    #print("такого нет")
money = 94
input("добро пожаловать в симулятор работы 1")
input("здесь тебе нужно работать и покупать вещи!")
input("...")
input("хочешь тайну?")
input("...")
input("не теряй все деньги иначе...")
for i in range(50):
    print(random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters))
while money > 0:
    comand = input("что ты хочешь зделать?(идти в магазин,идти работать,счёт,сражатся)")
    if comand == "идти в магазин":
        comand = "нечто"
        comand2 = "нечто"
        while comand2 != "выход" and money > 0:
            print("у вас ",money," монет!")
            
            input("вы пришли в магазин")
            input("вы видите кассиршу и спрашиваете *что можно купить?*")
            input("кассирша говорит *у нас есть хлеб,вода,чипсы,сок и семечки*")
            input("вы спрашиваете что сколько стоит")
            input("кассирша сказала *... ... ... ...  нуууу неа не скажу*")
            input("вы поняли что можно узнать как что стоит только покупая!")
            
            comand2 = input("что зделать?(купить,выход)")
            if comand2 == "купить":
                while cto != "отмена":
                    cto = input("что купить?(если не нужно то напиши отмена)")
                    if cto in items_shop.keys():
                        #проверка money >= cto
                        
                        money = money - items_shop[cto]
                        print("вы купили ",cto,"за ",items_shop[cto])
                        if money < 0:
                            print("у вас нету денег!!!")
                            input("нет что ты зделал!!")
                            break
                        print("у вас ",money," монет!") 
                    if cto == "отмена":
                        comand2 = "нечто"
                    
    
                   
    elif comand == "идти работать":
        comand2 = "нечто"
        rabota = "нечто"
        while rabota != "выход":
            rabota = input("вы точно готовы работать?(готов,выход)")
            if rabota == "готов":
                input("правила: вводи те буквы или цывры которые тебе пишут")
                for i in range(5):
                    ran1 = random.choice(string.ascii_letters)
                    ran2 = random.randint(1,3)
                    print(ran1)
                    otw1 = input("")
                    print(ran2)
                    otw2 = int(input(""))
                    if ran1 == otw1:
                        print("хорошо")
                    if ran2 == otw2:
                        print("хорошо")
                    if ran1 != otw1:
                        nepr = 1
                    if ran2 != otw2:
                        nepr = 1
                    
                if nepr == 0:
                    print("вы хорошо закончили работу!")
                    money = money + random.randint(15,45)
                    print("теперь у вас ",money," монет!")
                elif nepr == 1:
                    print("вы зделали чтото не правильное!")
    elif comand == "счёт":
        print("у вас ",money," монет!")
    elif comand == "сражатся":
        input("вы пошли в магазин оружии")
        input("вы пришли!")
        kupi_ory = "нечто"
        orywka = input("что вы хотите купить?")
        if orywka == "что купить?":
            input("*ой забыл* сказал продавец")
            input("*я продаю много чего но сначала*")
            input("*...*")
            input("продавец сказал что он продаёт*биту,крепкая биту,некрепкая биту*")
            kupi_ory = input("что вы хотите купить?")
            if kupi_ory in items_attack.keys():
                        #проверка money >= cto
                        
                        money = money - items_attack[kupi_ory]
                        print("вы купили ",kupi_ory,"за ",items_attack[kupi_ory])
                        yron = yron + items_attack[kupi_ory]
                        if money < 0:
                            print("у вас нету денег!!!")
                            input("нет что ты зделал!!")
                            break
                        print("у вас ",money," монет!") 
        if kupi_ory == "отмена":
            kupi_ory = "нечто"
            
        else:
            print("вы пошли сражатся!")
            input("ваш базовый урон ",yron)
            input("....")
            otm = 0
            while otm != 6:
                otm = otm + 1
                print("........................................................................................................................................................................")
            input("на вас напали!")
            input("это дерево!(чТО?)")
            input("вы атакуете дерево")
            
print("...")
