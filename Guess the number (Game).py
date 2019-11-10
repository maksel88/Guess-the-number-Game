from random import randint


print('Я загадал число от 1 до 100, угадай!')
cnt = 0  # счетчик (сколько было попыток)
t = list()  # записывает все числа, которые вводились

n = randint(0, 100)  # загаданное значение
print(n)


def get_int(prompt):  # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
    while True:
        try:
            global cnt, t
            cnt += 1
            value = int(input(prompt))
        except ValueError:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue
        if value == n:
            break
        if value in t:
            print('Вы уже вводили это число!', end=' ')
            if value < 0 or value > 100:
                print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            elif value > n:
                print('Загаданное число МЕНЬШЕ')
            elif value < n:
                print('Загаданное число БОЛЬШЕ.')
            continue
        elif value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            t.append(value)
            continue
        else:
            break
    t.append(value)
    return value


m = get_int('')  # вводимое значение


def set_min(m):  # вводимое значения меньше
    raznica = n - m
    if raznica > 20:
        return print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число БОЛЬШЕ.')
    t.append(m)


def set_max(m):  # вводимое значения больше
    raznica = m - n
    if raznica > 20:
        return print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число МЕНЬШЕ.')
    t.append(m)


while True:
    # m = get_int('')  # вводимое значение
    if m == n:
        print('Поздравляем! Вы угадали c {} попытки'.format(cnt))
        if input('Хочешь играть еще раз? "y|n"') == 'y':
            n = randint(0, 100)  # загаданное значение
            print(n)
            cnt = 0
            t.clear()
        # continue
        else:
            print('Спасибо за игру!')
            break
    elif m < n:
        set_min(m)
        m = get_int('')
    else:
        set_max(m)
        m = get_int('')
