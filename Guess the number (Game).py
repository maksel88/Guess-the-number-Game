from random import randint
from get_int import validate_input
from set_min import set_min
from set_max import set_max

print('Я загадал число от 1 до 100, угадай!')
# записывает все числа, которые вводились

<<<<<<< HEAD
random_number = randint(0, 100)  # загаданное значение
print(random_number)
previous_numbers = list()


user_input, cnt = validate_input(random_number, previous_numbers, '')  # вводимое значение


while True:
    if user_input < random_number:
        set_min(previous_numbers, random_number, user_input)
        user_input, cnt = validate_input(random_number, previous_numbers, '')
    elif user_input > random_number:
        set_max(user_input, random_number, previous_numbers)
        user_input, cnt = validate_input(random_number, previous_numbers, '')
    elif user_input == random_number:
        print('Поздравляем! Вы угадали c {} попытки'.format(cnt))
        if input('Хочешь играть еще раз? "y|n"') == 'y':
            random_number = randint(0, 100)  # загаданное значение
            print(random_number)
            cnt = 0
            previous_numbers.clear()
=======
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
>>>>>>> new_branch_2
        else:
            print('Спасибо за игру!')
            break
