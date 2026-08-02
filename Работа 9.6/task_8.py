user_text = input("Введите фрагмент послания: ")

reversed_text = " "

for current_symbol in user_text:
    reversed_text = current_symbol + reversed_text

if user_text == reversed_text:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
