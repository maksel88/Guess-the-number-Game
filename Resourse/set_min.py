def set_min(previous_numbers, user_input, random_number):  # вводимое значения меньше
    diff = user_input - random_number
    if diff > 20:
        print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < diff <= 20:
        print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= diff <= 10:
        print('Горячо! Загаданное число БОЛЬШЕ.')

    return previous_numbers
