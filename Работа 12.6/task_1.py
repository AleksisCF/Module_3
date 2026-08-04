import math

def summa_n(N):
    total = N * (N + 1) // 2
    print("Я знаю, что сумма чисел от 1 до", N, "равна", total)

N = int(input("Введите число: "))
summa_n(N)