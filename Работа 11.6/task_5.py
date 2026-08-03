import math

earth_volume = 1.08321 * 10 ** 12
R = float(input("Введите радиус теоретически возможной планеты: "))

planet_volume = (4 / 3) * math.pi * (R ** 3)

ratio = earth_volume / planet_volume

if ratio > 1:
    print("Объём планеты Земля больше в", round(ratio, 3), "раз")
else:
    print("Объём планеты Земля меньше в (1/", round(ratio, 3), ") =", round(1/ratio, 3), "раз")
