from random import randint
from get_int import input_check
from set_max import set_max
from set_min import set_min
from classes import Greeting

user = Greeting(input('Как Вас зовут? '))
user.print_greeting()

random_num = randint(0, 100)  # случайно загаданное значение
print(random_num)

cnt = 0  # счетчик попыток
box_num = []  # бокс для запоминания вводимых значений
while True:
    cnt += 1
    user_num, cnt = input_check('', box_num, cnt)  # вводимое пользователем значение
    box_num.append(user_num)
    if user_num == random_num:
        print(f"Поздравляю! Вы угадали c {cnt} попытки")
        user.print_play_one_more()
        if input('') == '+':
            cnt = 0
            random_num = randint(0, 100)
            print(random_num)
        else:
            print('Спасибо з а игру!')
            break
    elif user_num > random_num:
        set_max(random_num, user_num)
    elif user_num < random_num:
        set_min(user_num, random_num)
