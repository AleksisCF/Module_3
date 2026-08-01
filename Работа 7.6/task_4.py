N = int(input("Введите количество учеников в классе: "))

count_3 = 0
count_4 = 0
count_5 = 0

for i in range(N):
    grade = int(input("Введите оценку ученика (3, 4 или 5): "))
    if grade == 3:
        count_3 = count_3 + 1
    elif grade == 4:
        count_4 = count_4 + 1
    elif grade == 5:
        count_5 = count_5 + 1

if count_5 > count_4 and count_5 > count_3:
    print("Сегодня больше отличников.")
elif count_4 > count_5 and count_4 > count_3:
    print("Сегодня больше хорошистов.")
else:
    print("Сегодня больше троечников.")
