def pendulum():
    start = float(input("Введите начальную амплитуду: "))
    stop = float(input("Введите амплитуду остановки: "))

    if start <= 0 or stop <= 0:
        print("Ошибка: амплитуды должны быть положительными числами.")
        return

    count = 0
    amplitude = start

    while amplitude > stop:
        amplitude *= 0.916
        count += 1

    print("Маятник считается остановившимся через", count, "колебаний")

pendulum()