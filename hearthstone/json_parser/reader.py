import json
import os
import sqlite3

import json_parser.directory

data_root = json_parser.directory.data_root
file_name = json_parser.directory.file_name
json_file = data_root + file_name + '.json'
sql_file = data_root + file_name + '.db'


def get_json_cursor():
    return open(json_file, 'r', encoding='utf-8')


def get_json_data():
    cursor = get_json_cursor()
    data = json.load(cursor)
    cursor.close()
    return data


def remove_sql_data():
    try:
        os.remove(sql_file)
    except FileNotFoundError:
        pass


def get_sql_connection():
    return sqlite3.connect(sql_file)
