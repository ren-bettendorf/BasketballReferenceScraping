import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup

def scrapeHeader(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	table = soup.find('table', attrs={'id': 'per_game'})

	header = [header.text for header in table.findAll('th')]
	print(header)
	return header
	
def scrapeURL(url):
	#url = input("What basketball-reference player would you like to scrape their data?\n")
	#print("Connecting to website...")

	response = requests.get(url)
	#print("Succesful connection. Attempting to parse html")

	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	table = soup.find('table', attrs={'id': 'per_game'})

	#print("Succesfully parsed html. Now parsing table")
	header = [header.text for header in table.findAll('th')]
	tableData = {}
	for key in table.findAll('th'):
		tableData.setdefault(key.text, [])

	rowC = 1
	for row in table.findAll(attrs={'class':'full_table'}):
		colC = 1
		for i, cell in enumerate(row.findAll('td')):
			print("Header: " + header[i] + " Adding: " + cell.text.replace("\xa0★", "") + " to ("+str(rowC)+","+str(colC)+")")
			tableData[header[i]].append(cell.text.replace("\xa0★", ""))
			colC += 1
		rowC += 1
	json_string = json.dumps(tableData, indent=4)
	playerFile = soup.find('div', attrs={'id': 'info_box'}).h1.text.replace(" ", "") + "Stats.json"
	
	#print("Successfully parsed table.")

	with open(playerFile, "w") as outfile:
		outfile.write(json_string)
		
	#print("Successfully printed data to " + playerFile)
	
	return playerFile


	
scrapeURL("http://www.basketball-reference.com/players/c/curryst01.html")