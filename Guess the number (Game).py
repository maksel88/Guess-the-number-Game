import random

'''

'''

print('Игра "Угадай число"')
cnt = 0  # счетчик (сколько было попыток)
t = list()  # записывает все числа, которые вводились


n = random.randint(0, 100)  # загаданное число
print(n)


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            global cnt, t
            cnt += 1
        except ValueError:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            cnt += 1
            continue
        if value in t:
            print('Вы уже вводили это число!')
            continue
        elif value < 0:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            t.append(value)
            continue
        elif value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            t.append(value)
            continue
        else:
            break
    return value


m = get_int('')  # вводимое число
while m != n:
    if m < n:
        print('Неверно! Загаданное число БОЛЬШЕ.')
        t.append(m)
        m = get_int('')
    elif m > n:
        print('Неверно! Загаданное число МЕНЬШЕ.')
        t.append(m)
        m = get_int('')
print('Поздравляем! Вы угадали c {} попытки' .format(cnt))