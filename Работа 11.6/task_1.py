euro = float(input("Введите стоимость покупки в евро: "))

dollars = euro * 1.25
rubles = dollars * 60.87

print("Стоимость покупки в долларах:", round(dollars, 2))
print("Стоимость покупки в рублях:", round(rubles, 2))
