limit_number = int(input("Введите число: "))

current_number = 1

while current_number <= limit_number:
    cube_value = current_number ** 3
    print(cube_value)
    current_number = current_number + 1
