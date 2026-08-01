total_salary = 0

for month in range(1, 13):
    salary = int(input("Введите зарплату за " + str(month) + "-й месяц: "))
    total_salary = total_salary + salary

average_salary = total_salary / 12

print("Средняя зарплата за год равна", average_salary)
