# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello.Gui')
        self.resize(400,400)

        # Setting the layout
        layout=QVBoxLayout()
        self.setLayout(layout)

        # Adding the Widget
        self.Inputfield=QLineEdit()
        self.output=QTextEdit()
        button=QPushButton('Say Hello')
        button.clicked.connect(self.sayHello)

        # Adding the Widget to the layout
        layout.addWidget(self.Inputfield)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputtext =self.Inputfield.text()
        self.output.setText(f'Hello {inputtext}')



app=QApplication(sys.argv)
app.setStyleSheet('''
         QWidget {font-size: 15px}
         QPushButton {font-size: 10px}
         ''')
window=MyApp()
window.show()
app.exec()
