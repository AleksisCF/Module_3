levels = int(input("Введите количество уровней пирамиды: "))

current = 1
for row in range(1, levels + 1):
    
    print(" " * (levels - row), end = " ")
    
    for col in range(row):
        print(current, end = " ")
        current += 2
    print()

rows = int(input("Введите количество стпенек: "))
new_num = 1
for line in range(rows):
    space_count = rows - line - 1
    print("   " * space_count, end = "")
    for number in range(line + 1):
        print(new_num, end = '    ')
        new_num += 2
    print()