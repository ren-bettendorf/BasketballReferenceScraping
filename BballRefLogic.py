import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup
	
def scrapeURL(url):

	# Get HTML and table to scrap from url
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	table = soup.find('table', attrs={'id': 'per_game'})
	
	# Sets up Header values to be used later
	header = []
	tableData = {}
	for key in table.findAll('th'):
		header.append(key.text)
		tableData.setdefault(key.text, [])

	# Updates the lists in TableData with the correct data and removes the random non-ASCII values that are found for all-star
	for row in table.findAll(attrs={'class':'full_table'}):
		for i, cell in enumerate(row.findAll('td')):
			tableData[header[i]].append(cell.text.replace("\xa0★", ""))
	
	# Creates JSON String with players firstname + lastname + stats for where JSON file location
	json_string = json.dumps(tableData, indent=4)
	playerFile = soup.find('div', attrs={'id': 'info_box'}).h1.text.replace(" ", "") + "Stats.json"
	
	# Dumps to JSON String defined above
	with open(playerFile, "w") as outfile:
		outfile.write(json_string)
	
	# Returns File Location and header values for Table
	return [playerFile, header]