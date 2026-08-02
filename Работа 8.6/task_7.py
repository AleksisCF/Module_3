N = int(input("Введите N: "))
series_sum = 0
for n in range(N):
    elem = (-1) ** n * (1 / 2) ** n
    series_sum = series_sum + elem
print("Ответ:", series_sum)