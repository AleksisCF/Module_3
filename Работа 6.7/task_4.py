positive_count = 0
negative_count = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    elif number > 0:
        positive_count = positive_count + 1
    else:
        negative_count = negative_count + 1
print("Кол-во положительных чисел:", positive_count)
print("Кол-во отрицательных чисел:", negative_count)