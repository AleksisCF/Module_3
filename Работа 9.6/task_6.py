stalls_status = input("Введите строку из 10 символов a и b: ")

total_milk = 0
stall_number = 1

for current_stall in stalls_status:
    if current_stall == "b":
        total_milk = total_milk + 2 * stall_number
    stall_number = stall_number + 1

print("Всего молока за день:", total_milk, "литров")
