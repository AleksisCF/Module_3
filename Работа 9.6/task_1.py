# «Я стал новым пиратом!»

count = 0
for i in range(10):
    word = input("Введите слово: ")
    if word == "Карамба":
        print("Добро пожаловать на борт!")
        count += 1
    else:
        print("Не повезло!")
print("На корабль попадут", count, "человек")
