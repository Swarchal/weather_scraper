#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2

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



def get_time(soup_obj):
	'Extract time from BBC weather page current observations'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		time_string = found.find_all('', class_ = 'time')

	time = str(time_string)[len('<span class="time">') + 1 :-len('<\\span>') - 1]
	return time



def get_date(soup_obj):
	'Extract date from BBC weather current observations'
	observations = soup_obj.find_all('', class_= 'observations module')
	for found in observations:
		timestamp_str = str(found.find_all('', class_= 'timestamp'))

	date = timestamp_str[timestamp_str.find(',')+1:timestamp_str.find('</p>')]
	return date.strip()
