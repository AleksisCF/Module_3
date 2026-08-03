size = int(input("Введите размер матрицы: "))

for row in range(size):
    for col in range(size):
        print(row + col * 2, end="\t")
    print()
