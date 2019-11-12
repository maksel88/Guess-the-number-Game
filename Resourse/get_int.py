def validate_input(user_input, previous_numbers, prompt, cnt=0):
    # исправляет некоректный ввод данных, повторный ввод, ввод внедиапозона
    while True:
        try:
            cnt += 1
            value = int(input(prompt))
        except Exception:
            print("Некоректная запись. Нужно написать ЦЕЛОЕ ЧИСЛО!")
            continue

        if value in previous_numbers:
            print('Вы уже вводили это число!', end=' ')
            continue

        if value < 0 or value > 100:
            print('Некоректная запись. Число в НЕДИАПОЗОНА!')
            previous_numbers.append(value)
            continue
        break
    previous_numbers.append(value)
    return value, cnt