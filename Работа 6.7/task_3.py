number = int(input("Введите число: "))
digit_count = 0
while number > 0:
    number = number // 10
    digit_count = digit_count + 1
print("Количество цифр равно: ", digit_count)