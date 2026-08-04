def rock_paper_scissors():
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    computer_choice = "камень"
    print("Компьютер выбрал:", computer_choice)

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

def guess_the_number():
    secret = 7
    print("Я загадал число от 1 до 10. Попробуйте угадать!")
    while True:
        guess = int(input("Ваш вариант: "))
        if guess == secret:
            print("Поздравляю, вы угадали!")
            break
        else:
            print("Не угадали, попробуйте ещё раз.")

def mainMenu():
    while True:
        print("\nГлавное меню:")
        print("1 — Камень, ножницы, бумага")
        print("2 — Угадай число")
        print("3 — Выход")
        choice = input("Выберите игру: ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

mainMenu()
