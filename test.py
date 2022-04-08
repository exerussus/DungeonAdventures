from data import data_location


def change(decision):
    """Изменяет локацию"""
    actually = data_location['location']['actually_location']
    data_location['location']['actually_location'] = data_location['location'][actually][decision]


change('first')
print(data_location['location']['actually_location'])
