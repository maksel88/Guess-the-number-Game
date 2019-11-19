def set_max(user_num, random_num):  # вводимое значения больше
    raznica = user_num - random_num
    if raznica > 20:
        return print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число МЕНЬШЕ.')
    t.append(user_num)