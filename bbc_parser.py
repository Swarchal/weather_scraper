#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
import time
import re

def create_soup(url):
	'Create BeautifulSoup object from URL'
	response = urllib2.urlopen(url) # get html from URL
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup


def get_temp(soup_obj):
	'Extract current temperature from BBC weather page'
	# find current observations within html
	observations = soup_obj.find_all('', class_= 'observations module')

	# loop through observations looking for temp in celcius
	for found in observations:
		temp_string = str(found.find_all('',
			class_= "units-value temperature-value temperature-value-unit-c"))

	temp = [int(s) for s in temp_string if s.isdigit()][0]
	return temp



def get_datetime(soup_obj):
	'Extract datetime from BBC weather page current observations'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		time_string = found.find_all('', class_ = 'time')
		timestamp_str = str(found.find_all('', class_= 'timestamp'))

	time_ = str(time_string)[len('<span class="time">') + 1 :-len('<\\span>') - 1]
	time_pre = time_ + ':00'
	time_out = datetime.time(datetime.strptime(time_pre, '%X'))

	year = int(time.strftime("%Y"))
	date_ws = timestamp_str[timestamp_str.find(',')+1:timestamp_str.find('</p>')]
	date_pre = date_ws.strip()
	date_out = datetime.strptime(date_pre, '%A %d %B')
	date = datetime.date(date_out.replace(year = year))
	date_time = datetime.combine(date, time_out)
	return date_time


def get_humidity(soup_obj):
	'Extract humidity percentage'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		humid_string = str(found.find_all('', class_= "humidity"))
	humidity_list = [int(s) for s in humid_string if s.isdigit()]
	humidity = int(''.join(map(str, humidity_list))) # concat list of numbers
	return humidity


def get_windspeed(soup_obj):
	'Extract wind speed'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		ws_string = str(found.find_all('',
			class_="units-value windspeed-value windspeed-value-unit-mph"))
	ws_list = [int(s) for s in ws_string if s.isdigit()]
	windspeed = int(''.join(map(str, ws_list))) # concat list of numbers
	return windspeed


def get_winddirection(soup_obj):
	'Extract wind direction'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		dir_string = found.find_all('', class_= 'description blq-hide')
	direction = str(dir_string)[
	len('<span class="decription blq-hide">') + 2 :-len('<\\span>') - 1]
	return direction



def get_weather(soup_obj):
	'Extract weather, e.g cloudy or raining'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		weather_str = str(found.find_all('', class_= 'weather-type'))
	ans = re.findall(r'"(.+?)"', weather_str)[1] # get matches between ""
	return ans

def get_pressure(soup_obj):
	'Extract pressure in millibars'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		pressure_string = str(found.find_all('', class_='pressure'))
	pressure_list = [int(s) for s in pressure_string if s.isdigit()]
	pressure = int(''.join(map(str, pressure_list))) # concat list of numbers
	return pressure