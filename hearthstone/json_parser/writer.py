import sqlite3
import traceback

import json_parser


def write_database(data, cursor):
    for index in range(0, len(data)):
        entry = data[index]

        card = (
            index,
            get_value(entry, "id"),
            get_value(entry, "name"),
            get_value(entry, "text"),
            get_value(entry, "rarity"),
            get_value(entry, "type"),
            get_value(entry, "cost"),
            get_value(entry, "attack"),
            get_value(entry, "health"),
            get_value(entry, "collectible"),
            get_value(entry, "set"),
            get_value(entry, "faction"),
            get_value(entry, "artist"),
            get_value(entry, "flavor"),
            get_value(entry, "mechanics"),
            get_value(entry, "dust"),
            get_value(entry, "race"),
            get_value(entry, "playerClass"),
            get_value(entry, "howToEarn"),
            get_value(entry, "howToEarnGolden"),
            get_value(entry, "targetingArrowText"),
            get_value(entry, "durability"),
            get_value(entry, "entourage")
        )

        try:
            insert_entry(card, cursor)
        except sqlite3.OperationalError:
            print(traceback.format_exc())
            cursor.close()


def get_value(entry, field):
    return json_parser.formatter.get_key_value(entry, field)


def insert_entry(card, cursor):
    entry_count = 23
    param = '?'

    for index in range(1, entry_count):
        param += ',?'

    command = "INSERT INTO cards VALUES (" + param + ")"
    cursor.execute(command, card)


def create_database(connection):
    try:
        connection.cursor().execute('''CREATE TABLE cards (
                    key INTEGER PRIMARY KEY,
                    id TEXT,
                    name TEXT COLLATE NOCASE,
                    text TEXT COLLATE NOCASE,
                    rarity TEXT,
                    type TEXT,
                    cost INTEGER,
                    attack INTEGER,
                    health INTEGER,
                    collectible BOOLEAN,
                    cardSet TEXT,
                    faction TEXT,
                    artist TEXT,
                    flavor TEXT,
                    mechanics TEXT,
                    dust TEXT,
                    race TEXT COLLATE NOCASE,
                    playerClass TEXT,
                    howToEarn TEXT,
                    howToEarnGolden TEXT,
                    targetingArrowText TEXT,
                    durability INTEGER,
                    entourage TEXT
                    )''')
    except sqlite3.OperationalError:
        print(traceback.format_exc())
        connection.close()


def close_sql(connection):
    connection.commit()
    connection.close()
