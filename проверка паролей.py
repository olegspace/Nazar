
def num_check(pard):
    nums_here = False
    for symbol in pard:
        if symbol >= "0" and symbol <= "9":            
            nums_here=True
            break    
    return nums_here
def letters(l):
    letters = False
    for bykva in l:
        if bykva >= "a" and bykva <= "z":
            letters=True
            break
    return letters

def letterss(le):
    letters = False
    for bikva in le:
        if bikva >= "A" and bikva <= "Z":
            letters=True
            break
    return letters


def simba6(sim):
    simba6 = False
    for bivka in sim:
        sbv = len(p)
        if sbv >= 6:
            simba6=True
            break
    return simba6

def spet(sep):
    IQ = ["!","_","+","?","%","@","#","&","/"]
    spet = False
    for bivka in sep:
        if bivka in IQ:
            spet = True
            break
    return spet



p = input("введите пароль для добавление \n")
if not num_check(p):
    print("в пароли нет цифр!")
if not letters(p):
    print("нету букв или они не английские!")
if not letterss(p):
    print("нету ЗАГЛАВНЫХ букв или они не английские!")
if not simba6(p):
    print("нужно больше 6 симболов")
if not spet(p):
    print("нужны спец. значки! \n ☻☻ ")