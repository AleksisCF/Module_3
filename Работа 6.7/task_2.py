debtor_name = input("Введите имя: ")
debt_amount = int(input("Сколько рублей вы должны? "))
print(debtor_name, ", ваша задолженность составляет", debt_amount, "рублей")
while True:
    Summ = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    if Summ < debt_amount:
        print("Маловато,", debtor_name, ". Давайте ещё раз.")
    else:
        print("Отлично,", debtor_name, "! Вы погасили долг. Спасибо!")
        break