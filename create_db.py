#!/usr/bin/env python

import sqlite3 as sql

# db attributes
db_name = 'weather.sqlite'
table_name = 'Temp and Time'
temp_field = 'Temp(C)'
temp_field_type = 'REAL'
datetime_field = 'DateTime'
datetime_field_type = 'TEXT'

con = sql.connect(db_name)

c = con.cursor() # stupid thing

# create table with columns: id, datetime, temp
c.execute('''
    CREATE TABLE weather(id INTEGER PRIMARY KEY, datetime TEXT, temp REAL)
''')