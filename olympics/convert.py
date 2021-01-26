'''
Author: Aiden, Sky
Description: COnverting original csv files
Date: 2021-01-26 18:36:06
LastEditors: Tianyi Lu
LastEditTime: 2021-01-26 22:22:19
'''

import csv

def read_csv(filename):

    rows = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
    return rows[1:]

def read_csv_as_dict(filename):
    rows_dict = {}
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows_dict[row[1]] = row[0]
    return rows_dict


def write_from_athlete_events(filename, position_list, rows):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        unique_rows = []
        rows.sort(key=lambda x:x[position_list[0]])
        for row in rows:
            row_content = [row[x] for x in position_list]
            if len(unique_rows) == 0:
                unique_rows.append(row_content)
            elif row_content != unique_rows[-1]:
                unique_rows.append(row_content)

        for i, row in enumerate(unique_rows):
            csv_writer.writerow([i]+row)

def write_nocs_csv(filename, rows):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for i, row in enumerate(rows):
            csv_writer.writerow([i]+row)
            

def write_athletes_csv(rows):
    write_from_athlete_events('athletes.csv', [1,2,4,5], rows)

def write_games_csv(rows):
    write_from_athlete_events('games.csv', [8,9,10], rows)
    

def write_cities_csv(rows):
    write_from_athlete_events('cities.csv', [11], rows)

def write_events_csv(rows):
    write_from_athlete_events('events.csv', [13,12], rows)


def get_id(table_name, key):
    filename = table_name+'.csv'
    rows = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == key:
                return row[0]
        return None
        
def write_medals_csv(athletes_dict, game_dict, event_dict, rows):
    with open('medals.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for i, row in enumerate(rows):
            row_content = [athletes_dict[row[1]],
                           game_dict[row[8]],
                           event_dict[row[13]],
                           row[14]]
            csv_writer.writerow([i]+row_content)

def write_games_cities_csv(game_dict, city_dict, rows):
    with open('medals.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for i, row in enumerate(rows):
            row_content = [athletes_dict[row[1]],
                           game_dict[row[8]],
                           event_dict[row[13]],
                           row[14]]
            csv_writer.writerow([i]+row_content)
        

if __name__ == "__main__":
    athlete_rows = read_csv('athlete_events.csv')
    write_athletes_csv(athlete_rows)
    write_games_csv(athlete_rows)
    write_cities_csv(athlete_rows)
    write_events_csv(athlete_rows)

    noc_rows = read_csv('noc_regions.csv')
    write_nocs_csv('nocs.csv',noc_rows)

    athlete_dict = read_csv_as_dict('athletes.csv')
    game_dict = read_csv_as_dict('games.csv')
    city_dict = read_csv_as_dict('cities.csv')
    event_dict = read_csv_as_dict('events.csv')
    noc_dict = read_csv_as_dict('nocs.csv')

    write_medals_csv(athlete_dict, game_dict, event_dict, athlete_rows)

    # print(get_id('athletes', 'zzet nce'))

            
