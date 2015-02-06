import json
import sqlite3
import traceback
import os
import re

# obtain key value from dict
def GetValue (set, index, str):
	try:
		value = data[set][index][str]
	except KeyError:
		return "NULL"
	
	if str == "mechanics":
		mechStr = ""
		
		# concatenate all mechanic strings
		for x in range (0, len(value)):
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
jData = open('AllSets.json', 'r', encoding = 'utf-8')
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
					key integer primary key,
					cardSet text,
					id text,
					name text collate nocase,
					type text,
					cost integer,
					attack integer,
					health integer,
					mechanics text,
					text text collate nocase,
					playerClass text,
					rarity text,
					howToGet text,
					howToGetGold text,
					flavor text,
					artist text,
					collectible integer,
					race text collate nocase
					)''')
except sqlite3.OperationalError:
	print(traceback.format_exc())				

# card set declaration
set = ["Basic", "Curse of Naxxramas", "Expert", "Goblins vs Gnomes", "Promotion", "Reward"]
key = 1;

# populate database
for setIndex in range(0, len(set)):
	for index in range (0, len(data[set[setIndex]])):
		card = 	(	key,
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
			if not (card[5] == 'NULL' or card[16] == 'NULL'):
				c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", card)
					
		except sqlite3.OperationalError:
			print(traceback.format_exc())
			conn.close()
			
		key += 1

# commit all changes and close SQL connection
conn.commit()
conn.close()