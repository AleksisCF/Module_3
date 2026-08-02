start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг (отрицательный): "))
for x in range(end, start - 1, step):
    y = x**2 + 1
    print("В точке", x, "функция равна", y)