def maximum_of_two(a, b):
    if a > b:
        return a
    else:
        return b

def maximum_of_three(a, b, c):
    return maximum_of_two(maximum_of_two(a, b), c)

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))

print("Максимум из трёх чисел:", maximum_of_three(x, y, z))
