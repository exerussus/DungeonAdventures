from location import *

data_location = {

    'location': {
        '1': l1,
        '2': l2,
    },
}

data_equipment = {

    'armor': {
        'head': '',
        'body': '',
        'arms': '',
        'legs': '',
    },

    'weapon': {
        'first': '',
        'second': ''
    },

    'backpack': {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': ''
    },
}

data_characteristics = {

    'strength': 1,
    'dexterity': 1,
    'constitution': 1,
    'intellect': 1,
    'luck': 1,

}

data_status = {

    'max_health': data_characteristics['constitution'] * 2,
    'max_stamina': data_characteristics['dexterity'] * 2,
    'max_mind': data_characteristics['intellect'] * 2,

    'health': '',
    'stamina': '',
    'mind': '',

    'armor': {
        'head': 1 + data_equipment['armor']['head']['slash_dmg'],
        'body': 1,
        'arms': 1,
        'legs': 1,

    }
}

data_items = {
    'testID': {
        'id': '',
        'lvl': 1,
        'type': 'armor',
        'slot': 'body',
        'name': 'Кожаные ремни',
        'slash_dmg': 1,
        'blunt_dmg': 1,
        'piercing_dmg': 0,
        'mental_dmg': 5,
        'durability': 15,
        'description': {
            '0': 'Это можно надеть...',
            '5': 'Кожаный шлем. Вроде неплохо защищает.',
            '10': 'Кожаный шлем низкого качества. Защищает не слишком хорошо.',
            '15': 'Кожаный шлем. Немного защищает от дробящего и рубящего урона, но бесполезен для колющего.'
        }
    },
    'Пусто': {
        'id': '',
        'lvl': 0,
        'type': 'Пусто',
        'slot': 'Пусто',
        'name': 'Пусто',
        'slash_dmg': 0,
        'blunt_dmg': 0,
        'piercing_dmg': 0,
        'mental_dmg': 0,
        'durability': 99999,
        'description': {
            '0': 'Ничего. А нет, вот же! Ах, всё-таки ничего...',
            '5': 'Тут ничего нет.',
            '10': 'Тут ничего нет. Прям совсем.',
            '15': 'Если стоять и ничего не делать - тут так и останется пусто.'
        }
    }
}

data_abc = {
    'ABC': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
}
