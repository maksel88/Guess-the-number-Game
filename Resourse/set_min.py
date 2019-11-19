def set_min(user_num, random_num):  # вводимое значения меньше
    diff = random_num - user_num
    if diff > 20:
        print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < diff <= 20:
        print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= diff <= 10:
        print('Горячо! Загаданное число БОЛЬШЕ.')

