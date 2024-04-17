import sys
import PyQt6
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget,QLineEdit,QTextEdit,QPushButton,QTableWidget,QTableWidgetItem, QHeaderView,QVBoxLayout

class MyApp (QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        layout=QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Export Excel')

        self.table=QTableWidget()
        self.button=QPushButton('Export Excel')
        layout.addWidget(self.table)
        layout.addWidget(self.button)
        self.load_data()
        self.button.clicked.connect(self.export_excel)


    def export_excel(self):
        column_head=[]

        for j in range (0,self.table.columnCount()):
            column_head.append(self.table.horizontalHeaderItem(j).text())

        df =pd.DataFrame(columns=column_head)
        for i in range (0,self.table.rowCount()):
            for j in range (0,self.table.columnCount()):
                df.at[i,column_head[j]]=self.table.item(i,j).text()

        df.to_excel("exportexcel.xlsx")







    def load_data(self):
        n=300
        self.headlist=list('ABCDE')
        self.table.setRowCount(n)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(self.headlist)

        for row in range(n):
            for column in range (5):
                p=f"{row} - {column}"
                item=QTableWidgetItem(p)
                self.table.setItem(row,column,item)

app=QApplication(sys.argv)
window=MyApp()
window.show()
app.exec()