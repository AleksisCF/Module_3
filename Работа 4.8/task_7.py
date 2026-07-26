hours = int(input("Введите количество отработанных часов: "))
credit = int(input("Введите остаток по кредиту: "))
food_money = int(input("Введите траты на еду: "))

salary = (200 * hours / 2**3) + hours

total_needs = credit + food_money

if salary >= total_needs:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")