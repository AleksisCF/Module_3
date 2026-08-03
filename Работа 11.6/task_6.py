import math

horse_x = float(input("Введите координату коня по горизонтали: "))
horse_y = float(input("Введите координату коня по вертикали: "))

target_x = float(input("Введите координату точки по горизонтали: "))
target_y = float(input("Введите координату точки по вертикали: "))

if not (0 <= horse_x <= 0.8 and 0 <= horse_y <= 0.8 and 0 <= target_x <= 0.8 and 0 <= target_y <= 0.8):
    print("Клетки с такой координатой не существует")
else:
    horse_cell_x = int(horse_x * 10)
    horse_cell_y = int(horse_y * 10)
    target_cell_x = int(target_x * 10)
    target_cell_y = int(target_y * 10)

    print("Конь в клетке (", horse_cell_x,".",horse_cell_y, ").")
    print("Точка в клетке (", target_cell_x,".",target_cell_y, ").")

    dx = abs(horse_cell_x - target_cell_x)
    dy = abs(horse_cell_y - target_cell_y)

    if dx * dy == 2:
        print("Да, конь может ходить в эту точку.")
    else:
        print("Нет, конь не может ходить в эту точку.")