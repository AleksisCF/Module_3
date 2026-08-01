a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum_numbers = 0
count_numbers = 0

for number in range(a, b + 1):
    if number % 3 == 0:
        sum_numbers = sum_numbers + number
        count_numbers = count_numbers + 1

if count_numbers > 0:
    average = sum_numbers / count_numbers
    print("Среднее арифметическое чисел из отрезка [", a, ";", b, "] кратных 3 равно", average)
else:
    print("В диапазоне нет чисел, кратных 3.")
