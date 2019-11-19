from random import randint
from get_int import input_check
from set_max import set_max
from set_min import set_min

print('Я загадал число от 1 до 100, угадай!')
random_num = randint(0, 100)  # загаданное значение
print(random_num)

cnt = 0
box_num = []
while True:
    cnt += 1
    user_num, cnt = input_check('', box_num, cnt)
    box_num.append(user_num)
    if user_num == random_num:
        print(f"Поздравляем! Вы угадали c {cnt} попытки")
        if input('Если хочешь съиграть еще раз, нажму "+"') == '+':
            cnt = 0
            random_num = randint(0, 100)
            print(random_num)
        else:
            print('Спасибо за игру!')
            break
    elif user_num > random_num:
        set_max(random_num, user_num)
    elif user_num < random_num:
        set_min(user_num, random_num)
