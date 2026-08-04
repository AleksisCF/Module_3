def count_letters(text, digit, letter):
    digit_count = text.count(digit)
    letter_count = text.lower().count(letter.lower())
    print("Количество цифр", digit, ":", digit_count)
    print("Количество букв", letter, ":", letter_count)

text = input("Введите текст: ")
digit = input("Какую цифру ищем? ")
letter = input("Какую букву ищем? ")

count_letters(text, digit, letter)
