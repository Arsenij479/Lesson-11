import random

FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермантов': '15.10.1814',
                    'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семёнович Высоцкий': '25.01.1938',
                    'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович ': '17.09.1857',
                    'Сергей Павлович Коралёв': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                    'Андрей Николаевич Туполёв': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}

rounds = int(input('Сколько раз вы хотите играть?:'))
for i in range_(rounds):
    name,date = random.choice(list(FAMOUS_PEOPLE.itens()))
    ansaer = input(f'Когда родился {name}')
    if ansaer == date:
        print('Верно')
    else:
        print('Неверно')
print('Пока')
def game ():
    import random
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермантов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семёнович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович ': '17.09.1857',
                     'Сергей Павлович Коралёв': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполёв': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}

    rounds = int(input('Сколько раз вы хотите играть?:'))
    for i in range_(rounds):
        name, date = random.choice(list(FAMOUS_PEOPLE.itens()))
        ansaer = input(f'Когда родился {name}')
        if ansaer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')

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

