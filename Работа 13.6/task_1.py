def float_format(x):
    if x <= 0:
        print("Ошибка: число должно быть больше 0")
        return

    a = x
    b = 0

    while a >= 10:
        a /= 10
        b += 1

    while a < 1:
        a *= 10
        b -= 1

    print(f"Формат плавающей точки: x = {a} * 10 ** {b}")

x = float(input("Введите число: "))
float_format(x)
