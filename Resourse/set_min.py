def set_min(n, m):  # вводимое значения меньше
    raznica = n - m
    if raznica > 20:
        return print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число БОЛЬШЕ.')
    t.append(m)