experience_points = int(input("Введите количество очков опыта: "))

level = 1  # начальный уровень

if experience_points >= 5000:
    level = 4
elif experience_points >= 2500:
    level = 3
else:
    level = 2

print("Уровень персонажа:", level)
