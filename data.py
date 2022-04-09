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

}

data_items = {

    'testID': {
        'id': '21das2',
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

            '0': {

                'name': 'Пусто',
                'about': 'Ничего. А нет, вот же! Ах, всё-таки ничего...',

            },
            '5': {

                'name': 'Пусто',
                'about': 'Тут ничего нет.',

            },
            '10': {

                'name': 'Пусто',
                'about': 'Тут ничего нет. Прям совсем.',

            },
            '15': {

                'name': 'Пусто',
                'about': 'Если стоять и ничего не делать - тут так и останется пусто.',

            }
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

            '0': {

                'name': 'Пусто',
                'about': 'Ничего. А нет, вот же! Ах, всё-таки ничего...',

            },
            '5': {

                'name': 'Пусто',
                'about': 'Тут ничего нет.',

            },
            '10': {

                'name': 'Пусто',
                'about': 'Тут ничего нет. Прям совсем.',

            },
            '15': {

                'name': 'Пусто',
                'about': 'Если стоять и ничего не делать - тут так и останется пусто.',

            }
        }

    }
}

data_abc = {
    'ABC': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
}


item_lvl_1 = {

}

item_lvl_2 = {

}

item_lvl_3 = {

}


data_location = {

    'location': {

        '1': {
            'story': '',
            'choice': {
                '1': '',
                '2': '',
                '3': '',
                '4': '',
                'found': '',
            },
            'requirement': {
                '1': '0',
                '2': '0',
                '3': '0',
                '4': '0',
            },
            'inspection': {
                'true': '',
                'false': '',

            }
        },

        'actually_location': '1'
    }
}
