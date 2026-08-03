file_size = int(input("Укажите размер файла для скачивания (Мб): "))
speed = int(input("Какова скорость вашего соединения (Мб/с): "))

if file_size <= 0 or speed <= 0:
    print("Ошибка: размер файла и скорость должны быть положительными числами")
else:
    downloaded = 0
    seconds = 0

    while downloaded < file_size:
        seconds = seconds + 1
        downloaded = downloaded + speed
        if downloaded > file_size:
            downloaded = file_size
        percent = int(downloaded / file_size * 100)
        print("Прошло", seconds, "сек.", "Скачано", downloaded, "из", file_size, "Мб", "(", percent, "%)")

    print("Скачивание завершено за", seconds, "секунд")
