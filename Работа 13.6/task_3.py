def reverse_number(num):
    return int(str(num)[::-1])

N = int(input("Введите первое число: "))
K = int(input("Введите второе число: "))

rev_N = reverse_number(N)
rev_K = reverse_number(K)

print("Первое число наоборот:", rev_N)
print("Второе число наоборот:", rev_K)

sum_numbers = rev_N + rev_K
print("Сумма:", sum_numbers)

rev_sum = reverse_number(sum_numbers)
print("Сумма наоборот:", rev_sum)
