encrypted_message = input("Введите зашифрованное сообщение: ")

left_part = ""
right_part = ""
step_number = 1

for current_symbol in encrypted_message:
    if step_number % 2 == 1:
        left_part = left_part + current_symbol
    else:
        right_part = current_symbol + right_part
    step_number = step_number + 1

decrypted_message = left_part + right_part
print("Расшифрованное сообщение:", decrypted_message)
