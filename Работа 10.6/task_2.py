N = int(input("Введите число N: "))

for row in range(1, N + 1):
    for col in range(1, row + 1):
        print(row, end=" ")
    print()