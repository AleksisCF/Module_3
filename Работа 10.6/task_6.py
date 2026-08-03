height = int(input("Введите высоту пирамиды: "))

for row in range(1, height + 1):
    for space in range(height - row):
        print(" ", end = "")
    for hash in range(2 * row - 1):
        print("#", end = "")
    print()
