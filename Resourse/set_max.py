<<<<<<< HEAD
def set_max(random_number, user_input, previous_numbers):  # вводимое значения больше
    diff = random_number - user_input
    if diff > 20:
        print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < diff <= 20:
        print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= diff <= 10:
        print('Горячо! Загаданное число МЕНЬШЕ.')
    return previous_numbers
=======
def set_max(user_num, random_num):  # вводимое значения больше
    raznica = user_num - random_num
    if raznica > 20:
        return print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число МЕНЬШЕ.')
    t.append(user_num)
>>>>>>> new_branch_2
