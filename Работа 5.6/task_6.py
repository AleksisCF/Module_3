apartment_price = int(input("Введите стоимость квартиры (в млн): "))
apartment_area = int(input("Введите площадь квартиры (в м2): "))

if apartment_area >= 100 and apartment_price <= 10:
    print("Квартира подходит: просторная и в бюджете.")
elif apartment_area >= 80 and apartment_price <= 7:
    print("Квартира подходит: чуть меньше, но в бюджете.")
else:
    print("Квартира не подходит.")