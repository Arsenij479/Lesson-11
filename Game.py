
print('Добро пожаловать в игру викторина')
name = input('Как тебя зовут?')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    victory_game()
elif answer == 'Нет':
    print(('Ну давай готовься тогда)'))
else:
    print('Не могу понять, что ты хочешь от меня)')

