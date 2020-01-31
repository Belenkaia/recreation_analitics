import pandas as pd
from model_constants import const


def get_map_dictionary():
    zone_id = '№ зоны'
    average_trafic = 'средняя заполненность'
    chair_space_amount = 'Кол-во сидячих мест'
    table_space_amount = 'Кол-во ноутбуков/мест за столиками'
    power_sockets_amount = 'Кол-во розеток'
    classrooms = 'Аудитории'
    classroom_distances = 'Дистанция до аудитории'
    popularity = 'популярность'
    map_df = pd.read_csv(const.map_table_file, sep='\t')

    map_df[table_space_amount] = map_df[table_space_amount].fillna(0)
    map_df[power_sockets_amount] = map_df[power_sockets_amount].fillna(0)

    map_dict = {}
    for i, row in map_df.iterrows():
        try:
            new_zone = {}
            new_zone['size'] = row[chair_space_amount] + row[table_space_amount]
            new_zone['powerSockets'] = row[power_sockets_amount]
            new_zone['traffic'] = row[average_trafic]
            new_zone['popularity'] = row[popularity]
            new_zone['classrooms'] = []
            classroom_ids = str(row[classrooms]).split(',')
            distances = str(row[classroom_distances]).split(',')
            for classroom in zip(classroom_ids, distances):
                new_zone['classrooms'].append({
                    'id': classroom[0].strip(),
                    'distance': classroom[1].strip()
                })
            map_dict[row[zone_id]] = new_zone
        except KeyError as err:
            print(err)
    return map_dict


def