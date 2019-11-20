<<<<<<< HEAD
def validate_input(user_input, previous_numbers, prompt, cnt=0):
    # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
=======
def get_int(random_num, box_num, prompt, cnt=0):  # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
>>>>>>> new_branch_2
    while True:
        try:
            cnt += 1
            value = int(input(prompt))
        except Exception:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue
<<<<<<< HEAD

        if value in previous_numbers:
            print('Вы уже вводили это число!', end=' ')
=======
        if value == random_num:
            break
        if value in box_num:
            print('Вы уже вводили это число!', end=' ')
            if value < 0 or value > 100:
                print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            elif value > random_num:
                print('Загаданное число МЕНЬШЕ')
            elif value < random_num:
                print('Загаданное число БОЛЬШЕ.')
>>>>>>> new_branch_2
            continue

        if value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
<<<<<<< HEAD
            previous_numbers.append(value)
            continue
        break
    previous_numbers.append(value)
=======
            box_num.append(value)
            continue
        else:
            break
    box_num.append(value)
>>>>>>> new_branch_2
    return value, cnt