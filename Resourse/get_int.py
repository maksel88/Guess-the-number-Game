def get_int(n, t, prompt, cnt=0):  # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
    while True:
        try:
            cnt += 1
            value = int(input(prompt))
        except Exception:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue
        if value == n:
            break
        if value in t:
            print('Вы уже вводили это число!', end=' ')
            if value < 0 or value > 100:
                print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            elif value > n:
                print('Загаданное число МЕНЬШЕ')
            elif value < n:
                print('Загаданное число БОЛЬШЕ.')
            continue
        elif value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            t.append(value)
            continue
        else:
            break
    t.append(value)
    return value
    return cnt