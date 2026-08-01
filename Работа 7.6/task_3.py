n = int(input("Введите число: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Факториал числа", n, "равен", factorial)
