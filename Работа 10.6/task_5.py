seqNum = int(input("Введите количество чисел: "))
maxSum = 0
maxNumber = 0

for i in range(seqNum):
    print("Введите число:", end = " ")
    number = int(input())
    digitSum = 0
    temp = number
    while temp > 0:
        digitSum += temp % 10
        temp //= 10
    if digitSum > maxSum:
        maxSum = digitSum
        maxNumber = number

print("Число с наибольшей суммой цифр:", maxNumber)
print("Сумма его цифр:", maxSum)