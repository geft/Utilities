import json
import os
import re
import sqlite3
import traceback


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
jData = open('AllSets.json', 'r', encoding='utf-8')
data = json.load(jData)

# close JSON data when done
jData.close()

# remove database if exists
try:
    os.remove("cards.db")
except FileNotFoundError:
    pass

# connect to SQL database
conn = sqlite3.connect('cards.db')

# create a cursor object to execute SQL commands
c = conn.cursor()

# create database table
try:
    c.execute('''	CREATE TABLE cards (
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
					race TEXT COLLATE nocase,
					collection BOOLEAN
					)''')
except sqlite3.OperationalError:
    print(traceback.format_exc())

# card set declaration
cardSet = ["Basic",
           "Blackrock Mountain",
           "Credits",
           "Classic",
           "Curse of Naxxramas",
           "Debug",
           "Goblins vs Gnomes",
           "Promotion",
           "Reward",
           "System",
           "Tavern Brawl",
           "The Grand Tournament",
           "League of Explorers"]
key = 1

# populate database
for setIndex in range(0, len(cardSet)):
    for index in range(0, len(data[cardSet[setIndex]])):
        card = (    key,
                    cardSet[setIndex],
                    GetValue(cardSet[setIndex], index, "id"),
                    GetValue(cardSet[setIndex], index, "name"),
                    GetValue(cardSet[setIndex], index, "type"),
                    GetValue(cardSet[setIndex], index, "cost"),
                    GetValue(cardSet[setIndex], index, "attack"),
                    GetValue(cardSet[setIndex], index, "health"),
                    GetValue(cardSet[setIndex], index, "mechanics"),
                    GetValue(cardSet[setIndex], index, "text"),
                    GetValue(cardSet[setIndex], index, "playerClass"),
                    GetValue(cardSet[setIndex], index, "rarity"),
                    GetValue(cardSet[setIndex], index, "howToGet"),
                    GetValue(cardSet[setIndex], index, "howToGetGold"),
                    GetValue(cardSet[setIndex], index, "flavor"),
                    GetValue(cardSet[setIndex], index, "artist"),
                    GetValue(cardSet[setIndex], index, "collectible"),
                    GetValue(cardSet[setIndex], index, "race"),
                    "1"
        )

        try:
            # if null cost or null collectible or non-collectible
            if not (card[5] == 'NULL' or card[16] == 'NULL' or card[16] == 0):
                c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", card)

        except sqlite3.OperationalError:
            print(traceback.format_exc())
            conn.close()

        key += 1

# commit all changes and close SQL connection
conn.commit()
conn.close()
