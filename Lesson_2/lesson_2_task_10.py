import math

x = int(input('Минимальная сумма вклада 1000 рублей. Введите сумму вклада: '))
if x < 1000:
    x = 1000

y = int(input('Минимальный срок 1 год. Максимальный 50 лет. Введите срок вклада: '))
if y < 1:
    y = 1
if y > 50:
    y = 50

def bank():
    procent = 0.1
    sum = x*(1+procent)**y
    print("Ваш рассчет равен", math.floor(sum) , "рублей")
bank()