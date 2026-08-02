total_buckwheat = 100
for month in range(1, total_buckwheat // 4 + 1):
    remaining = total_buckwheat - month * 4
    print("Через", month, "месяц(а) останется", remaining, "кг гречки")