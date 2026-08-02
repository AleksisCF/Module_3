reverse_timer = int(input("Задайте время до обнуления таймера (в секундах): "))
for second in range(reverse_timer, -1, -1):
    print("Осталось секунд:", second)
    user_choice = int(input("Хотите остановить разогрев? (1 — Да, 0 — Нет): "))
    if user_choice == 1:
        print("Ваша еда готова, можете забрать.")
        print("Таймер был прерван на секунде:", second)
        break
else:
    print("Ваша еда готова, осторожно горячо!")
