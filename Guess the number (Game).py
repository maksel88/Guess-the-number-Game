print('Игра угадай число')
cnt = 1  # счетчик (сколько было попыток)
t = []  # записывает все числа, которые вводились
n = 80  # загаданное число


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            global cnt
            cnt += 1
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
        m = get_int('')
        continue
    elif m < n:
        print('Неверно! Загаданное число БОЛЬШЕ.')
        t.append(m)
        m = get_int('')
    elif m > n:
        print('Неверно! Загаданное число МЕНЬШЕ.')
        t.append(m)
        m = get_int('')
print('Поздравляем! Вы угадали c ', cnt, ' попытки')