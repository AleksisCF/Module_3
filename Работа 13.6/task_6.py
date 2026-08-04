def danger(x):
    return x**3 - 3*x**2 - 12*x + 10

def find_depth(eps):
    left, right = 0, 4
    while right - left > eps:
        mid = (left + right) / 2
        if danger(mid) == 0:
            return mid
        if danger(left) * danger(mid) < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

eps = float(input("Введите максимально допустимый уровень опасности: "))
depth = find_depth(eps)
print("Приблизительная глубина безопасной кладки:", depth, "м")
