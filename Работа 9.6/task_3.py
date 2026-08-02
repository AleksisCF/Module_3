rows = int(input("Введите кол-во рядов: "))
seats = int(input("Введите кол-во сидений в ряде: "))
space = int(input("Введите кол-во метров между рядами: "))
print("Сцена")
for row_number in range(rows):
    print("======= " + "* " * seats + "=======")
    for s in range(space):
        print()