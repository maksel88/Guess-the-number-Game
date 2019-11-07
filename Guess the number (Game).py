print('Игра угадай число')
count=1
n=80
m=int(input())
# try:
#     m=int(input())
# except ValueError:
#     print('Некоректная запись. Попробуй еще раз!')
#     m=int(input())
#     count += 1
# except ValueError:
#     print('Это что ещё такое? Eще раз!')
#     m = int(input())
#     count += 1
while m!=n:
    if 100 < m <= 0:
        print('Вы ввели число вне диапозона. Попробуйте еще раз.')
        count += 1
        m = int(input())
    elif m < n:
        print('Неверно! Загаданное число БОЛЬШЕ.')
        count+=1
        m=int(input())
    elif m > n:
        print('Неверно! Загаданное число МЕНЬШЕ.')
        count+=1
        m = int(input())
print ('Поздравляем! Вы угадали c ' , count , ' попытки')