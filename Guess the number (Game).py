import random

print('Игра "Угадай число"')
cnt = 0  # счетчик (сколько было попыток)
t = list()  # записывает все числа, которые вводились

n = random.randint(0, 100)  # загаданное число
print(n)


def get_int(prompt):
    while True:
        try:
            global cnt, t
            cnt += 1
            value = int(input(prompt))
        except ValueError:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue
        if value in t:
            print('Вы уже вводили это число! ')
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


def set_min(m):
    raznica = n - m
    if raznica > 20:
        return print('Холодно! Загаданное число БОЛЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число БОЛЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число БОЛЬШЕ.')
    t.append(m)


def set_max(m):
    raznica = m - n
    if raznica > 20:
        return print('Холодно! Загаданное число МЕНЬШЕ.')
    if 10 < raznica <= 20:
        return print('Тепло! Загаданное число МЕНЬШЕ.')
    elif 1 <= raznica <= 10:
        return print('Горячо! Загаданное число МЕНЬШЕ.')
    t.append(m)


m = get_int('')  # вводимое число
while m != n:
    if m < n:
        set_min(m)
        m = get_int('')
    elif m > n:
        set_max(m)
        m = get_int('')
print('Поздравляем! Вы угадали c {} попытки'.format(cnt))
