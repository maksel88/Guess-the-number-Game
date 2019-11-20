def input_check(prompt, box_num, cnt):  # проверка вводимого значения
    while True:
        try:
            value = int(input(prompt))
        except Exception:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            cnt += 1
            continue
        if value in box_num:
            print('Вы уже вводили это число!', end=' ')
        elif value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!', end=' ')
        break
    return value, cnt
