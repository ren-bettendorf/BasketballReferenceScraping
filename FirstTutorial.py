import csv
import requests
from bs4 import BeautifulSoup



url = input("What basketball-reference player would you like to scrape their data?\n")
print("Connecting to website...")
response = requests.get(url)
print("Succesful connection. Attempting to parse html")
html = response.content
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', attrs={'id': 'totals'})

print("Succesfully parsed html. Now parsing table")

list_of_rows = []
headerNames = []
for row in table.findAll('th'):
    headerNames.append(row.text)
list_of_rows.append(headerNames)

count = 0
for row in table.findAll('tr'):
    if count == 0:
        count += 1
        continue
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        text = text.replace('\xa0★', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

playerName = soup.find('div', attrs={'id': 'info_box'}).h1.text
playerName = playerName.replace(" ", "")
playerFile = playerName + "Stats.csv"
print("Successfully parsed table.")
with open(playerFile, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)

print("Successfully printed data to " + playerFile)
