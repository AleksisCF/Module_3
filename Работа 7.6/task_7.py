N = int(input("Введите количество карточек: "))

total_sum = N * (N + 1) // 2
entered_sum = 0

for i in range(N - 1):
    card_number = int(input("Введите номер оставшейся карточки: "))
    entered_sum = entered_sum + card_number

missing_card = total_sum - entered_sum

print("Номер пропавшей карточки:", missing_card)
