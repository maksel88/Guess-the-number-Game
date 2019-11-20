class Greeting:

    def __init__(self, name):
        self.name = name

    def print_greeting(self):
        print(f'Привет {self.name}. Давайте поиграем? Я загадал число от 1 до 100, угадай!')

    def print_play_one_more(self):
        print(f'Слушай {self.name}, если хочешь съиграть еще раз нажми "+"')