from classes import *
from data import *
import random

def write_text(text):
    writer = Text(text)
    writer.write()


def selfinit():
    """ Присваивание значения класса Menu в переменную menu """
    menu = Menu('')


def random_id_generation(item):
    """ Генерация ключа новой вещи """
    random_value = ''
    key = 1
    while key == 1:
        rand1 = random.choice(data_abc['ABC'])
        rand2 = random.choice(data_abc['ABC'])
        rand3 = random.choice(data_abc['ABC'])
        rand4 = random.choice(data_abc['ABC'])
        rand5 = random.choice(data_abc['ABC'])
        rand6 = random.choice(data_abc['ABC'])
        rand7 = random.choice(data_abc['ABC'])
        rand8 = random.choice(data_abc['ABC'])
        random_value = rand1 + rand2 + rand3 + rand4 + rand5 + rand6 + rand7 + rand8
        if random_value not in data_items:
            data_items[random_value] = item
            key = 0
            break
    return random_value
