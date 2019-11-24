class Greeting:

    def __init__(self, name):
        self.name = name

    def print_greeting(self):
        print(f'Привет {self.name}. Давайте поиграем? Я загадал число от 1 до 100, угадай!')

    def print_play_one_more(self):
        print(f'Слушай {self.name}, если хочешь сыграть еще раз нажми "+", если нет, то любую другую клавишу')

    def print_play_again(self):
        print('Я  снова загадал число от 1 до 100, угадай!')

    def good_buy(self):
        print(f'Спасибо за игру {self.name}!')