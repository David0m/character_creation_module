from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')