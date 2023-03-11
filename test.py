import random
def generate():
    num1 = random.randint(1,9)
    num2 = random.randint(0,9)
    while num1 == num2:
        num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    while num3 == num2 or num3 == num1:
        num3 =random.randint(0,9)
    print(num1,num2,num3)
    
    return str(num1)+str(num2)+str(num3)

def equals(str1,str2):
    if str1 == str2:
        return True
    else:
        return False
    
    

Zagadano = generate()
BBOD = input("что загодали??????????? ")

if equals(Zagadano, BBOD):
    print("вы угадали")
else:
    print("не угадали!")
print("Загадали: ", Zagadano)