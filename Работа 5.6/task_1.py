experience_points = int(input("Введите количество очков опыта: "))

if experience_points >= 5000:
    level = 4
elif experience_points >= 2500:
    level = 3
elif experience_points >= 1000:
    level = 2
else:
    level = 1

print("Ваш уровень:", level)
