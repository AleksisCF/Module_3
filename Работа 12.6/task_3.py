def sum_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    print("Сумма цифр числа:", total)

def max_digit(num):
    maximum = max(int(d) for d in str(num))
    print("Максимальная цифра числа:", maximum)

def min_digit(num):
    minimum = min(int(d) for d in str(num))
    print("Минимальная цифра числа:", minimum)

while True:
    number = int(input("Введите число: "))
    action = input("Что сделать? (сумма/максимум/минимум/выход): ")

    if action == "сумма":
        sum_digits(number)
    elif action == "максимум":
        max_digit(number)
    elif action == "минимум":
        min_digit(number)
    elif action == "выход":
        print("Работа завершена.")
        break
    else:
        print("Неизвестное действие, попробуйте снова.")
