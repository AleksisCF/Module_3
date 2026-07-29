num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 == num2 == num3:
    print("Совпадают все три числа: 3")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Совпадают два числа: 2")
else:
    print("Все числа разные: 0")