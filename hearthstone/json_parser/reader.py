import json
import os
import sqlite3


def get_json_cursor(json_file):
    return open(json_file, 'r', encoding='utf-8')


def get_json_data(json_file):
    cursor = get_json_cursor(json_file)
    data = json.load(cursor)
    cursor.close()
    return data


def remove_sql_data(sql_file):
    try:
        os.remove(sql_file)
    except FileNotFoundError:
        pass


def get_sql_connection(sql_file):
    return sqlite3.connect(sql_file)
