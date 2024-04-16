import sys
import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit,QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QTextEdit, QVBoxLayout
import pandas as pd

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Execl App')
        self.resize(400,400)
        layout=QVBoxLayout()
        self.setLayout(layout)

        self.table=QTableWidget()
        self.button=QPushButton("Load Data")
        self.filepath='school.xlsx'
        self.sheetname='SCHOOL'
        self.button.clicked.connect(self.load_data)

        layout.addWidget(self.table)
        layout.addWidget(self.button)

    def load_data(self):
        df = pd.read_excel('deevyansh.xlsx')
        if(df.shape[0]==0):
            return
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for row in df.iterrows():
            values=row[1]
            for col_index,value in enumerate(values):
                tableitem= QTableWidgetItem(str(value))
                self.table.setItem(row[0],col_index,tableitem)







app=QApplication(sys.argv)

filepath='school.xlsx'
sheetname='School'



window=MyApp()
window.show()
app.exec()