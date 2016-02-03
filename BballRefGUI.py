import json
from pprint import pprint
import sys
from BballRefLogic import scrapeURL
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QTableWidget, QTableWidgetItem, QHeaderView)

class BballRefScrapeUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
        
        
	def initUI(self):
	
		self.setWindowTitle('Player Stats')
		
		grid = QGridLayout()
		grid.setSpacing(10)

		self.setLayout(grid) 
		
		JSONFile, header, playerName = scrapeURL("http://www.basketball-reference.com/players/c/curryst01.html")
		
		tableData = json.loads(JSONFile)
		tableWidget = QTableWidget(len(tableData[header[1]]),len(header))
		urlEdit = QLineEdit()
		playerNameLabel = QLabel("Current Player Stats: " + playerName)
		
		# Create Table from tableData keys, values
		for col, key in enumerate(header):
			for row, item in enumerate(tableData[key]):
				newItem = QTableWidgetItem(item)
				tableWidget.setItem(row, col, newItem)
				
		tableWidget.setHorizontalHeaderLabels(header)
		tableWidget.resizeColumnsToContents()
		tableWidget.resizeRowsToContents()
		
		horizontalHeader = tableWidget.horizontalHeader()
		verticalHeader = tableWidget.verticalHeader()
		
		self.setGeometry(300,300,len(horizontalHeader)*32 + 55, len(verticalHeader)*32 + 40)
		grid.addWidget(urlEdit, 0, 0)
		grid.addWidget(playerNameLabel, 1, 0)
		grid.addWidget(tableWidget, 2, 0)
        
		self.show()
	
def main():
    app = QApplication(sys.argv)
    ex = BballRefScrapeUI()
    app.exec_()
	
if __name__ == '__main__':
    main()
