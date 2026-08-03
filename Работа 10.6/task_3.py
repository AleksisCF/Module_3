height = int(input("Введите высоту рамки: "))
width = int(input("Введите ширину рамки: "))

for row in range(height):
    for col in range(width):
        if row == 0 or row == height - 1:   # верх и низ
            print("-", end = " ")
        elif col == 0 or col == width - 1: # левая и правая границы
            print("|", end = " ")
        else:
            print(" ", end = " ")
    print()
