from game import game_func

print('Добро пожаловать в игру Кто Хочет стать Миллионером')
print('Хотите начать новую игру?')
print('1: Да')
print('2: Нет')

user_decision = int(input('Введите ответ (1/2): '))

game_func(user_decision)

