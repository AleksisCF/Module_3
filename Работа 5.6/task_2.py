x = int(input("Введите число X: "))

if x > 0:
    y = x - 12
elif x == 0:
    y = 5
else:  # значит x < 0
    y = x ** 2

print("Значение функции Y:", y)
