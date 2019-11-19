def set_min(random_num, user_num):  # вводимое значения меньше
    raznica = random_num - user_num
    if raznica > 20:
        return print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число БОЛЬШЕ.')
    box_num.append(user_num)