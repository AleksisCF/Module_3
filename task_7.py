Number = int(input("Введите четырёхзначное число: "))

digit1 = Number // 1000
digit2 = (Number // 100) % 10
digit3 = (Number // 10) % 10
digit4 = Number % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)