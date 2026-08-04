import math

def gcd(a, b):
    return math.gcd(a, b)

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

print("Наибольший общий делитель чисел", x, "и", y, "равен", gcd(x, y))
