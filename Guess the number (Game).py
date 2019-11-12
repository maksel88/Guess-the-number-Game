from random import randint
from get_int import get_int
from set_min import set_min
from set_max import set_max

print('Я загадал число от 1 до 100, угадай!')
# записывает все числа, которые вводились

n = randint(0, 100)  # загаданное значение
print(n)
t = list()


m = get_int(n, t, '')  # вводимое значение


while True:
    if m < n:
        set_min(n, m)
        m = get_int(n, t, '')
    elif m > n:
        set_max(m, n)
        m = get_int(n, t, '')
    elif m == n:
        print('Поздравляем! Вы угадали c {} попытки'.format(cnt))
        if input('Хочешь играть еще раз? "y|n"') == 'y':
            n = randint(0, 100)  # загаданное значение
            print(n)
            cnt = 0
            t.clear()
        else:
            print('Спасибо за игру!')
            break
