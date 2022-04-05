import time
from data import *
from items import *

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Text:

    def __init__(self, text):
        self.text = text

    def write(self):
        for i in self.text:
            time.sleep(0.02)
            print(i, end='')
        print('\n')


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class Menu:

    def __init__(self, menu_choice):
        """Инициация класса Menu"""

        self.menu_choice = menu_choice

    def main(self):
        """ Запуск главного меню """
        while True:
            time.sleep(0.7)
            print('*** DUNGEON MUSTERS ***\n'
                  '1. Новая игра\n'
                  '2. Загрузка\n'
                  '3. Настройки\n'
                  '4. Статистика\n'
                  '0. Выход\n')
            time.sleep(0.7)
            self.menu_choice = input('Выберите действие: ')
            time.sleep(0.7)
            if self.menu_choice not in ('1', '2', '3', '4', '0'):
                time.sleep(0.7)
                print('Пожалуйста, выберите действие из списка...')
                continue
            else:
                pass


class Item:
    """Управление предметами"""
    def __init__(self, item):
        self.item = item

    def put_on(self):
        """Надеть предмет"""
        old_item = data_equipment[['equipment'][self.item['slot']]]
        data_equipment[['equipment'][self.item['slot']]] = self.item

        data_equipment['backpack'][self.item] =    # дописать: удаление предмета из бэкпака
        for slot in data_equipment['backpack']:
            if data_equipment['backpack'][slot] == 'Пусто':
                data_equipment['backpack'][slot] = old_item

    def take_off(self):
        """Снять предмет"""
        data_equipment[['equipment'][self.item['slot']]] = 'Пусто'
        for slot in data_equipment['backpack']:
            if data_equipment['backpack'][slot] == 'Пусто':
                data_equipment['backpack'][slot] = self.item
