tasks_total = 0
wife_called = False
print("Начался восьмичасовой рабочий день.")
for hour in range(1, 9):
    print(hour, "-й час")
    tasks = int(input("Сколько задач решит Максим? "))
    tasks_total = tasks_total + tasks

    call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if call == 1:
        wife_called = True
print("Рабочий день закончился. Всего выполнено задач:", tasks_total)
if wife_called:
    print("Нужно зайти в магазин.")
