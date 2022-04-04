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

}


