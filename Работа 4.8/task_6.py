Number_1 = int(input("Кубик Кости: "))
Number_2 = int(input("Кубик владельца: "))
if Number_1 >= Number_2:
    print(Number_1 - Number_2)
    print("Игрок платит")
else:
    print("Сумма:", Number_1 + Number_2)
    print("Владелец платит")
