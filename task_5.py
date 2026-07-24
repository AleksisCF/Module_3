QuantityMinutes = int(input("Введите количество минут: "))

Hours = QuantityMinutes // 60
Remaining_minutes = QuantityMinutes % 60

print("В часах: ", Hours)
print("Остаток минут: ", Remaining_minutes)