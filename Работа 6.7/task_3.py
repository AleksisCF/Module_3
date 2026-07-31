number = int(input("Введите число: "))
digit_count = 0
while number > 0:
    number = number // 10
    digit_count = digit_count + 1
print("Количество цифр равно: ", digit_count)
number = int(input("Введите число: "))
if number == 0:
    digit_count = 1
else:
    digit_count = 0
    if number < 0:
        number = -number
    while number > 0:
        number = number // 10
        digit_count = digit_count + 1
print("Количество цифр равно:", digit_count)
