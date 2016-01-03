#!/usr/bin/env python

import sqlite3 as sql
import time
import bbc_parser as bbc

URL = 'http://www.bbc.co.uk/weather/2650225'

db_name = 'weather.sqlite'

start_time = time.time()
while True:

	soup = bbc.create_soup(URL)
	datetime = bbc.get_datetime(soup)
	temp = bbc.get_temp(soup)
	humidity = bbc.get_humidity(soup)
	wind_speed = bbc.get_windspeed(soup)
	wind_direction = bbc.get_winddirection(soup)
	weather = bbc.get_weather(soup)
	pressure = bbc.get_pressure(soup)
  
	con = sql.connect(db_name)
	c = con.cursor()
	values = [datetime, temp, humidity, wind_speed, wind_direction, weather, pressure]
	c.execute('INSERT INTO weather VALUES (?,?,?,?,?,?,?)', values)
	con.commit()
	con.close()
	print ' - Entry added for', datetime

	time.sleep(360.0 - ((time.time() - start_time) % 360.0))