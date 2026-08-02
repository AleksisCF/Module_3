user_message = input("Введите текст: ")
symbol_index = 1

for current_symbol in user_message:
    if current_symbol == "*":
        print("Символ '*' стоит на позиции", symbol_index)
        break
    else:
        symbol_index = symbol_index + 1
