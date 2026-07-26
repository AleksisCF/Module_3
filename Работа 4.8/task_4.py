FirstPrice = int(input("Введите цену: "))
SecondPrice = int(input("Введите цену: "))
ThirdPrice = int(input("Введите цену: "))
Total = FirstPrice + SecondPrice + ThirdPrice
if Total > 10000:
    Discount = Total * 10 / 100
    Total = Total - Discount
print("Итоговая сумма: ", Total)