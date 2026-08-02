boys_count = int(input("Введите количество мальчиков: "))
girls_count = int(input("Введите количество девочек: "))
if abs(boys_count - girls_count) > 1:
    print("Нет решения")
else:
    result = ""
    if boys_count >= girls_count:
        while boys_count > 0 or girls_count > 0:
            if boys_count > 0:
                result = result + "B"
                boys_count = boys_count - 1
            elif girls_count > 0:
                result = result + "G"
                girls_count = girls_count - 1
    else:
        while boys_count > 0 or girls_count > 0:
            if girls_count > 0:
                result = result + "G"
                girls_count = girls_count - 1
            elif boys_count > 0:
                result = result + "B"
                boys_count = boys_count - 1
    print("Ответ:", result)