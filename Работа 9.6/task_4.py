x_position = 8
y_position = 10

while True:
    command = input("Марсоход находится на позиции " 
                    + str(x_position) + ", " + str(y_position) 
                    + ", введите команду: ")
    command = command.upper()

    if command == "W" and y_position < 20:
        y_position = y_position + 1
    elif command == "S" and y_position > 1:
        y_position = y_position - 1
    elif command == "A" and x_position > 1:
        x_position = x_position - 1
    elif command == "D" and x_position < 15:
        x_position = x_position + 1
    # если команда не подходит или упёрся в стену — позиция не меняется
