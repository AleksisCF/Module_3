def count_numbers(num):
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp //= 10
    return count

def change_number(num):
    digits = count_numbers(num)
    last_digit = num % 10
    first_digit = num // 10 ** (digits - 1)
    between_digits = num % 10 ** (digits - 1) // 10
    return last_digit * 10 ** (digits - 1) + between_digits * 10 + first_digit

def main():
    first_n = int(input("Введите первое число: "))
    if count_numbers(first_n) < 3:
        print("В первом числе меньше трёх цифр.")
        return

    second_n = int(input("Введите второе число: "))
    if count_numbers(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
        return

    first_changed = change_number(first_n)
    second_changed = change_number(second_n)

    print("Изменённое первое число:", first_changed)
    print("Изменённое второе число:", second_changed)
    print("Сумма чисел:", first_changed + second_changed)

main()
