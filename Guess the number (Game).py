from random import randint
from get_int import get_int
from set_min import set_min
from set_max import set_max

print('Я загадал число от 1 до 100, угадай!')
# записывает все числа, которые вводились

random_num = randint(0, 100)  # загаданное значение
print(random_num)
box_num = list()


user_num, cnt = get_int(random_num, box_num, '')  # вводимое значение


while True:
    if user_num < random_num:
        set_min(random_num, user_num)
        user_num = get_int(random_num, box_num, '')
    elif user_num > random_num:
        set_max(user_num, random_num)
        user_num = get_int(random_num, box_num, '')
    elif user_num == random_num:
        print('Поздравляем! Вы угадали c {} попытки'.format(cnt))
        if input('Хочешь играть еще раз? "y|n"') == 'y':
            random_num = randint(0, 100)  # загаданное значение
            print(random_num)
            cnt = 0
            box_num.clear()
        else:
            print('Спасибо за игру!')
            break
