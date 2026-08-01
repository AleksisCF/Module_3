positive_even_count = 0

for i in range(10):
    number = int(input("Введите число: "))
    if number > 0 and number % 2 == 0:
        positive_even_count = positive_even_count + 1

print("Количество положительных чётных чисел:", positive_even_count)