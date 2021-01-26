'''
Author: Aiden, Sky
Description: COnverting original csv files
Date: 2021-01-26 18:36:06
LastEditors: Tianyi Lu
LastEditTime: 2021-01-26 21:06:17
'''

import csv

def read_athlete_events():
    """
    Load books from books.csv
    :return: A list of book objects
    """
    rows = []
    with open('athlete_events.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
    return rows[1:]

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

def write_athletes_csv(rows):
    write_from_athlete_events('athletes.csv', [1,2,4,5], rows)

def write_games_csv(rows):
    write_from_athlete_events('games.csv', [8,9,10], rows)
    

def write_cities_csv(rows):
    write_from_athlete_events('cities.csv', [11], rows)

def write_events_csv(rows):
    write_from_athlete_events('events.csv', [13,12], rows)

def write_game_city_csv(rows):
    write_game_city("game_city.csv", rows)

def write_game_city(filename,rows):
    i =0
    game_rows = read_rows("game")
    city_rows = read_rows("city")
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        uniqueList = []
        for row in rows:
            i+= 1
            #print(i)
            if row[8]+row[11] not in uniqueList:
                uniqueList.append(row[8] + row[11])
                csv_writer.writerow([get_id_from_table(row[8], game_rows) ,get_id_from_table(row[11], city_rows)])

def read_rows(file_category):
    rows = []
    if file_category == "game":
        filename = 'games.csv'
    if file_category == "city":
        filename = 'cities.csv'
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
    return rows
    

def get_id_from_table(object_name, rows):
    for row in rows:
        if object_name in row:
            print(row)
            
            return row[0]


if __name__ == "__main__":
    rows = read_athlete_events()
    write_athletes_csv(rows)
    write_games_csv(rows)
    write_cities_csv(rows)
    write_events_csv(rows)
    write_game_city_csv(rows)
            
