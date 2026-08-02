a = int(input("Введите число a (начало отрезка): "))
b = int(input("Введите число b (конец отрезка): "))
c = int(input("Введите число c (делитель): "))
sum_numbers = 0
count_numbers = 0
for number in range(a, b + 1):
    if number % c == 0:
        sum_numbers = sum_numbers + number
        count_numbers = count_numbers + 1
if count_numbers > 0:
    average = sum_numbers / count_numbers
    print("Среднее арифметическое чисел из отрезка [", a, ";", b, "] кратных", c, "равно", average)
else:
    print("В диапазоне нет чисел, кратных", c)