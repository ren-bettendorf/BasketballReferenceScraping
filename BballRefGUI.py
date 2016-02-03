import json
from pprint import pprint
import sys
from BballRefLogic import scrapeURL
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QTableWidget, QTableWidgetItem)

class BballRefScrapeUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
        
        
	def initUI(self):
	
		self.setGeometry(300, 300, 800, 400)
		self.setWindowTitle('Review')
		
			
		grid = QGridLayout()
		grid.setSpacing(10)

		self.setLayout(grid) 
		
		JSONFile, header = scrapeURL("http://www.basketball-reference.com/players/c/curryst01.html")
        
		with open(JSONFile) as dataFile:
			tableData = json.loads(dataFile.read())
		
		tableWidget = QTableWidget(len(tableData[header[0]]),len(header))
		urlEdit = QLineEdit()
		
		for col, key in enumerate(tableData.keys()):
			for row, item in enumerate(tableData[key]):
				newItem = QTableWidgetItem(item)
				tableWidget.setItem(row, col, newItem)
				
		tableWidget.setHorizontalHeaderLabels(header)
		tableWidget.resizeColumnsToContents()
		tableWidget.resizeRowsToContents()
		
		grid.addWidget(urlEdit, 1, 0)

		grid.addWidget(tableWidget, 2, 0)
        
		self.show()
	
def main():
    app = QApplication(sys.argv)
    ex = BballRefScrapeUI()
    app.exec_()
	
if __name__ == '__main__':
    main()
