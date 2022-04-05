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

    key = 1
    while key == 1:
        rand1 = random.choice(data_abc['abc_and_numbers'])
        rand2 = random.choice(data_abc['abc_and_numbers'])
        rand3 = random.choice(data_abc['abc_and_numbers'])
        rand4 = random.choice(data_abc['abc_and_numbers'])
        rand5 = random.choice(data_abc['abc_and_numbers'])
        rand6 = random.choice(data_abc['abc_and_numbers'])
        rand7 = random.choice(data_abc['abc_and_numbers'])
        rand8 = random.choice(data_abc['abc_and_numbers'])
        random_value = rand1 + rand2 + rand3 + rand4 + rand5 + rand6 + rand7 + rand8
        if random_value not in data_items:
            data_items[random_value] = item
            key = 0
            break
