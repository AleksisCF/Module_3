debtors_count = int(input("Введите количество должников: "))
total_debt = 0
for debtor_number in range(0, debtors_count, 5):
    print("Должник с номером", debtor_number)
    debt_amount = int(input("Сколько должны? "))
    total_debt = total_debt + debt_amount
print("Общая сумма долга:", total_debt)