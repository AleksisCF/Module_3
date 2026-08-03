seqNum = int(input("Введите количество чисел: "))
primeCount = 0

for i in range(seqNum):
    print("Введите число:", end = " ")
    number = int(input())
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            primeCount += 1

print("Количество простых чисел в последовательности:", primeCount)
