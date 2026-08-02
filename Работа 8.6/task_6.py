educational_grant = int(input("Введите степендию: "))
expenses = int(input("Введите расходы: "))
total_parent_money = 0
for month in range(1, 11):
    shortage = expenses - educational_grant
    total_parent_money = total_parent_money + shortage
    print("месяц", month, "траты", expenses, "не хватает", shortage)
    expenses = expenses * 1.03
print("Нужно попросить у родителей", round(total_parent_money, 2), "рублей")