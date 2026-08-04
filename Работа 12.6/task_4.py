def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    print("Число наоборот:", reversed_num)

while True:
    number = int(input("Введите число: "))
    if number == 0:
        print("Программа завершена!")
        break
    reverse_number(number)
