First_number = int(input("Введите первое число: "))
Second_number = int(input("Введите второе число: "))

ValueNumber1 = First_number % 100
ValueNumber2 = Second_number % 100

result = ValueNumber1 + ValueNumber2
print("Сумма двух последних цифр: ", result)