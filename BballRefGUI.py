import sys
import json
from pprint import pprint
from BballRefLogic import (scrapeURL, scrapeHeader)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QTableWidget, QString)

class BballRefScrapeUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
        
        
	def initUI(self):
		JSONFile = scrapeURL("http://www.basketball-reference.com/players/c/curryst01.html")
        
		with open(JSONFile) as dataFile:
			tableData = json.loads(dataFile.read())
		
		tableWidget = QTableWidget(len(tableData),len(tableData['0']))
		urlEdit = QLineEdit()
		header = scrapeHeader("http://www.basketball-reference.com/players/c/curryst01.html")
		
		for index in range(len(header)):
			tableWidget.setHorizontalHeaderItem(index, QString(header[index]))
			
		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(urlEdit, 1, 0)

		grid.addWidget(tableWidget, 2, 0)
        
		self.setLayout(grid) 
        
		self.setGeometry(300, 300, 800, 400)
		self.setWindowTitle('Review')    
		self.show()
	
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = BballRefScrapeUI()
    sys.exit(app.exec_())
