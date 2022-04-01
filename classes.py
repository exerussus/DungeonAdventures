import time

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

    def __init__(self, menu_coise):
        '''Инициация класса Menu'''
        self.menu_choise = menu_coise

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
            self.menu_choise = input('Выберите действие: ')
            time.sleep(0.7)
            if self.menu_choise not in ('1', '2', '3', '4', '0'):
                time.sleep(0.7)
                print('Пожалуйста, выберите действие из списка...')
                continue
            else:
                pass
