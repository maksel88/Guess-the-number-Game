print('Игра угадай число')
cnt = 1  # счетчик (сколько было попыток)
t = []  # записывает все числа, которые вводились
n = 80  # загаданное число


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Некоректная запись. Нужно написать ЧИСЛО!")
            continue
        if value < 0:
            print("Некоректная запись. Нужно написать ПОЛОЖИТЕЛЬНОЕ число!")
            continue
        else:
            break
    return value


m=get_int('') # вводимое число
while m != n:
    if m in t:
        print('Вы уже вводили это число!')
        cnt += 1
        m = get_int('')
        continue
    if 100 < m <= 0:
        print('Вы ввели число вне диапозона. Попробуйте еще раз.')
        cnt += 1
        t.append(m)
        m = get_int('')
    elif m < n:
        print('Неверно! Загаданное число БОЛЬШЕ.')
        cnt += 1
        t.append(m)
        m = get_int('')
    elif m > n:
        print('Неверно! Загаданное число МЕНЬШЕ.')
        cnt += 1
        t.append(m)
        m = get_int('')
print('Поздравляем! Вы угадали c ', cnt, ' попытки')
