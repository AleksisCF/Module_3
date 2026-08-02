user_text = input("Введите текст: ")

current_length = 0
max_length = 0

for current_symbol in user_text:
    if current_symbol != " ":
        current_length = current_length + 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_length = 0

if current_length > max_length:
    max_length = current_length

print("Самое длинное слово, букв:", max_length)
