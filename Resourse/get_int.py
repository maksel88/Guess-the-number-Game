def get_int(random_num, box_num, prompt, cnt=0):  # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
    while True:
        try:
            cnt += 1
            value = int(input(prompt))
        except Exception:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue
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
            continue
        elif value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            box_num.append(value)
            continue
        else:
            break
    box_num.append(value)
    return value
    return cnt