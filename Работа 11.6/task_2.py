import math

n = int(input("Введите кол-во чисел: "))

for i in range(n):
    x = float(input("Введите число: "))

    if x > 0:
        x_round = math.ceil(x)
        print("x =", x_round, "log(x) =", math.log(x_round))
    elif x < 0:
        x_round = math.floor(x)
        print("x =", x_round, "exp(x) =", math.exp(x_round))
    else:
        print("x = 0, логарифм и экспонента не определены")
