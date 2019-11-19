def set_max(random_num, user_num):  # вводимое значения больше
    diff = user_num - random_num
    if diff > 20:
        print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < diff <= 20:
        print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= diff <= 10:
        print('Горячо! Загаданное число МЕНЬШЕ.')
