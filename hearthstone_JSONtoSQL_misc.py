import json
import sqlite3
import traceback
import os
import re

# obtain key value from dict
def GetValue(set, index, str):
    try:
        value = data[set][index][str]
    except KeyError:
        return "NULL"

    if str == "mechanics":
        mechStr = ""

        # concatenate all mechanic strings
        for x in range(0, len(value)):
            mechStr = mechStr + value[x] + ","

        # remove last comma
        if mechStr[-1] == ",":
            mechStr = mechStr[:-1]

        return mechStr

    # format card text
    if str == "text":
        value = re.sub(r'(<b>|</b>|<i>|</i>)|[$,.:#]', '', value)

    return value

# load JSON data and parse into a dict object
jData = open('AllSets.json', 'r')
data = json.load(jData)

# close JSON data when done
jData.close()

# remove database if exists
try:
    os.remove("cards_misc.db")
except:
    pass

# connect to SQL database
conn = sqlite3.connect('cards_misc.db')

# create a cursor object to execute SQL commands
c = conn.cursor()

# create database table
try:
    c.execute('''	CREATE TABLE cards_misc (
					key INTEGER PRIMARY KEY,
					cardSet TEXT,
					id TEXT,
					name TEXT COLLATE nocase,
					type TEXT,
					cost INTEGER,
					attack INTEGER,
					health INTEGER,
					mechanics TEXT,
					text TEXT COLLATE nocase,
					playerClass TEXT,
					rarity TEXT,
					howToGet TEXT,
					howToGetGold TEXT,
					flavor TEXT,
					artist TEXT,
					collectible INTEGER,
					race TEXT COLLATE nocase
					)''')
except sqlite3.OperationalError:
    print(traceback.format_exc())

# card set declaration
set = ["Basic", "Curse of Naxxramas", "Expert", "Goblins vs Gnomes", "Promotion", "Reward"]
key = 1

# populate database
for setIndex in range(0, len(set)):
    for index in range(0, len(data[set[setIndex]])):
        card = (    key,
                    set[setIndex],
                    GetValue(set[setIndex], index, "id"),
                    GetValue(set[setIndex], index, "name"),
                    GetValue(set[setIndex], index, "type"),
                    GetValue(set[setIndex], index, "cost"),
                    GetValue(set[setIndex], index, "attack"),
                    GetValue(set[setIndex], index, "health"),
                    GetValue(set[setIndex], index, "mechanics"),
                    GetValue(set[setIndex], index, "text"),
                    GetValue(set[setIndex], index, "playerClass"),
                    GetValue(set[setIndex], index, "rarity"),
                    GetValue(set[setIndex], index, "howToGet"),
                    GetValue(set[setIndex], index, "howToGetGold"),
                    GetValue(set[setIndex], index, "flavor"),
                    GetValue(set[setIndex], index, "artist"),
                    GetValue(set[setIndex], index, "collectible"),
                    GetValue(set[setIndex], index, "race")
        )

        try:
            if card[5] == 'NULL' or card[16] == 'NULL':
                c.execute("INSERT INTO cards_misc VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", card)

        except sqlite3.OperationalError:
            print(traceback.format_exc())
            conn.close()

        key += 1

# commit all changes and close SQL connection
conn.commit()
conn.close()