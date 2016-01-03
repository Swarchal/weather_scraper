#!/usr/bin/env python

import sqlite3 as sql

db_name = 'weather.sqlite'

con = sql.connect(db_name)

c = con.cursor() # stupid thing

# create table with columns: id, datetime, temp
c.execute('''
    CREATE TABLE weather(id INTEGER PRIMARY KEY,
    	datetime TEXT,
    	temp REAL,
    	humidity REAL,
    	wind_speed REAL,
    	wind_direction TEXT,
    	weather TEXT,
    	pressure REAL)
''')