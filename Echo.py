import sys

import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()
        self.setLayout(layout)
        self.resize(400,400)


        lineedits={}

        lineedits['NoEcho']=QLineEdit()
        lineedits['NoEcho'].setEchoMode(QLineEdit.EchoMode.NoEcho)
        lineedits['NoEcho'].setPlaceholderText('No Echo')
        lineedits['NoEcho'].textChanged.connect(self.printv)

        lineedits['Normal'] = QLineEdit()
        lineedits['Normal'].setEchoMode(QLineEdit.EchoMode.Normal)
        lineedits['Normal'].setPlaceholderText('Normal')
        lineedits['Normal'].textChanged.connect(self.printv)

        lineedits['Password'] = QLineEdit()
        lineedits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        lineedits['Password'].setPlaceholderText('Password')
        lineedits['Password'].textChanged.connect(self.printv)

        lineedits['PasswordonEdits']=QLineEdit()
        lineedits['PasswordonEdits'].setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        lineedits['PasswordonEdits'].setPlaceholderText('PasswordEchoonedits')
        lineedits['PasswordonEdits'].textChanged.connect(self.printv)




        for _,item in lineedits.items():
            layout.addWidget(item)
    def printv(self,v):
        print(v)


app=QApplication(sys.argv)
window=MyApp()
window.show()
app.exec()
