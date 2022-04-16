import time
from data import *
from items import *
from function import *

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

    def main(self):
        """ Запуск главного меню """
        while True:
            time.sleep(0.7)
            print('*** DUNGEON ADVENTURES ***\n'
                  '1. Новая игра\n'
                  '2. Загрузка\n'
                  '3. Настройки\n'
                  '4. Статистика\n'
                  '0. Выход\n')
            time.sleep(0.7)
            menu_choice = input('Выберите действие: ')
            time.sleep(0.7)
            if menu_choice not in ('1', '2', '3', '4', '0'):
                time.sleep(0.7)
                print('Пожалуйста, выберите действие из списка...')
                continue
            else:
                pass

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class Item:
    """ Управление предметами """

    def put_on(self, item):
        """ Надеть предмет """
        old_item = data_equipment[['equipment'][item['slot']]]  # old_item = ключ уже надетой вещи
        data_equipment[['equipment'][item['slot']]] = item  # Вставляем в слот ключ вещи
        data_equipment['backpack'][item] = old_item   # Вставляем снятую вещь на место надетой в backpack

    def take_off(self, item):
        """ Снять предмет """
        old_item = data_equipment[['equipment'][item['slot']]]
        data_equipment[['equipment'][item['slot']]] = data_items['Пусто']
        empty_key = 1
        for slot in data_equipment['backpack']:
            if empty_key == 1 and data_equipment['backpack'][slot] == data_items['Пусто']:
                data_equipment['backpack'][slot] = item
                empty_key = 0
        if empty_key == 1:
            while True:
                answer = input('В рюкзаке нет места. Выбросить вещь?')
                if answer == 'Да' or answer == 'да' or answer == 'ага' or answer == 'АГА':
                    break
                if answer == 'Нет' or answer == 'нет' or answer == 'не' or answer == 'Не':
                    data_equipment[['equipment'][item['slot']]] = old_item
                print('Пожалуйста, подтвердите, выкинуть вещь, или нет...')

    def naming(self, item):
        """ Осмотр вещи """
        if data_characteristics['intellect'] < 5:
            data_items[item]['name'] = data_items[item]['description']['0']['name']
            data_items[item]['about'] = data_items[item]['description']['0']['about']
        if data_characteristics['intellect'] < 10:
            data_items[item]['name'] = data_items[item]['description']['5']['name']
            data_items[item]['about'] = data_items[item]['description']['5']['about']
        if data_characteristics['intellect'] < 15:
            data_items[item]['name'] = data_items[item]['description']['10']['name']
            data_items[item]['about'] = data_items[item]['description']['10']['about']
        if data_characteristics['intellect'] > 14:
            data_items[item]['name'] = data_items[item]['description']['15']['name']
            data_items[item]['about'] = data_items[item]['description']['15']['about']

    def take(self, item):
        """ Получение предмета """
        item = random_id_generation(item)
        self.naming(item)

    def delete(self, item):
        data_items.pop(item)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class Location:

    # def __init__(self, decision):
    #     self.decision = decision

    def change(self, decision):
        """Изменяет локацию"""
        actually = data_location['location']['actually_location']
        data_location['location']['actually_location'] = data_location['location'][actually][decision]


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
