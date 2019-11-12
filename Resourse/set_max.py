def set_max(random_number, user_input, previous_numbers):  # вводимое значения больше
    diff = random_number - user_input
    if diff > 20:
        print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < diff <= 20:
        print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= diff <= 10:
        print('Горячо! Загаданное число МЕНЬШЕ.')
    return previous_numbers
