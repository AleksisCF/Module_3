for number in range(10, 100):
    tens = number // 10
    ones = number % 10
    if number == 3 * tens * ones:
        print(number)