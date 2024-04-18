import sys
import os
import time
import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget,QPushButton,QVBoxLayout, QHeaderView, QTableWidgetItem, QLineEdit, QTextEdit, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector as sql
import pymysql

class AdminApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin Window')
        self.resize(400,400)
        self.label1=QLabel('Welcome Admin')
        self.label2=QLabel('')
        self.button1=QPushButton('See Data')
        self.button2=QPushButton('Make Result')
        self.button1.clicked.connect(self.show_data)
        self.button2.clicked.connect(self.makeresult)
        layout=QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.label1)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        layout.addWidget(self.table)
        layout.addWidget(self.label2)

    def show_data(self):
        label=['USERNAME','BID_VALUE']
        self.table.setHorizontalHeaderLabels(label)
        db=pymysql.connect(host='localhost',user='root',password='c24466fb',database='SCHOOL')
        for i in range (3):
            cursor=db.cursor()
            query="SELECT Username FROM logindata LIMIT 1 OFFSET %s"
            cursor.execute(query,(i,))
            result=cursor.fetchone()
            print(result)
            table_item = QTableWidgetItem(str(result[0]))
            self.table.setItem(i,0,table_item)
        for i in range (3):
            cursor=db.cursor()
            query="SELECT Bid_Value FROM logindata LIMIT 1 OFFSET %s"
            cursor.execute(query,(i,))
            result=cursor.fetchone()
            print(result)
            table_item = QTableWidgetItem(str(result[0]))
            self.table.setItem(i,1,table_item)
        return

    def makeresult(self):
        largest=0
        db = pymysql.connect(host='localhost', user='root', password='c24466fb', database='SCHOOL')
        off=0
        for i in range (3):
            cursor=db.cursor()
            query="SELECT Bid_Value FROM logindata LIMIT 1 OFFSET %s"
            cursor.execute(query,(i,))
            result=cursor.fetchone()
            if(int(result[0]))>largest:
                largest=int(result[0])
                off=i
        cursor = db.cursor()
        query = "SELECT Username FROM logindata LIMIT 1 OFFSET %s"
        cursor.execute(query, (off,))
        result = cursor.fetchone()
        username=result[0]
        self.label2.setText(f'Winner is the {username} with the {largest} bid')
        return

class MainApp(QWidget):
    def __init__(self,username):
        super().__init__()
        self.setWindowTitle(f'Main App{username}')
        self.resize(400,200)
        layout=QVBoxLayout()
        self.label1=QLabel(f"Welcome {username}")
        self.label2=QLabel("{Set the Bid for today}")
        self.status=QLabel('')
        self.setLayout(layout)
        self.button=QPushButton('Finalize the bid')
        layout.addWidget(self.button)
        self.lineedit=QLineEdit()
        self.lineedit.setPlaceholderText('Enter your bid value')
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button)
        layout.addWidget(self.status)
        self.username=username
        self.button.clicked.connect(self.storeinfo)



    def storeinfo(self,username):
        db = pymysql.connect(host='localhost', user='root', passwd='c24466fb', database='SCHOOL')
        cursor = db.cursor()
        query = "UPDATE logindata SET Bid_Value = %s WHERE Username = %s"
        bid_value = self.lineedit.text()
        cursor.execute(query, (bid_value, self.username))
        db.commit()
        self.status.setText('Bid value updated successfully')
        cursor.close()
        db.close()



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Window')
        self.resize(600,200)
        layout=QGridLayout()
        self.setLayout(layout)

        self.labels={}
        self.lineedits={}
        self.labels['Username']=QLabel('Username')
        self.labels['Password']=QLabel('Password')
        self.labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        self.lineedits['Username']=QLineEdit()
        self.lineedits['Password']=QLineEdit()
        self.lineedits['Username'].setPlaceholderText('Username')
        self.lineedits['Password'].setPlaceholderText('Password')
        self.lineedits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.labels['Username'],   0, 0, 1 , 1)
        layout.addWidget(self.lineedits['Username'],    0, 1, 1, 3)
        layout.addWidget(self.labels['Password'],   1, 0, 1,1)
        layout.addWidget(self.lineedits['Password'],    1,1,1,3)

        self.button=QPushButton('Login')
        layout.addWidget(self.button, 2, 3, 1,1)
        self.status=QLabel('Status')
        layout.addWidget(self.status,2,0,1,2)

        self.button.clicked.connect(self.checkCredentials)

    def connectdB(self):
        db=pymysql.connect(host='localhost',user='root',passwd='c24466fb',database='SCHOOL')
        self.status.setText('Connection Set')

        if not db.open:
            self.status.setText('No Connection not found')

        cursor=db.cursor()
        cursor.execute("""
        CREATE TABLE logindata(
            id INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(255),
            Password VARCHAR(255),
            Bid_Value INT
        )
        """)
        data=('Admin','223',0)
        insert_query="INSERT INTO logindata (Username,Password,Bid_Value) VALUES(%s,%s,%s)"
        cursor.execute(insert_query,data)
        data=('John','225',0)
        insert_query = "INSERT INTO logindata (Username,Password,Bid_Value) VALUES(%s,%s,%s)"
        cursor.execute(insert_query, data)
        data = ('Deevyansh', '224', 0)
        insert_query = "INSERT INTO logindata (Username,Password,Bid_Value) VALUES(%s,%s,%s)"
        cursor.execute(insert_query, data)
        db.commit()
        cursor.close()

    def checkCredentials(self):
        # self.connectdB()
        try:
            username = self.lineedits['Username'].text()
            password = self.lineedits['Password'].text()

            db = pymysql.connect(host='localhost', user='root', passwd='c24466fb', database='SCHOOL')
            cursor = db.cursor()

            query = "SELECT * FROM logindata WHERE Username=%s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                if result[2] == password:
                    self.status.setText("Password is correct")
                    if not (username =="Admin"):
                        self.app1 = MainApp(username)
                        self.app1.show()
                        self.close()
                    else:
                        self.app1=AdminApp()
                        self.app1.show()
                        self.close()
                else:
                    self.status.setText("Password is not correct")
            else:
                self.status.setText("Username not found")

            cursor.close()
            db.close()

        except Exception as e:
            self.status.setText("Error: {}".format(str(e)))


app=QApplication(sys.argv)
window=LoginWindow()
window.show()
app.exec()
