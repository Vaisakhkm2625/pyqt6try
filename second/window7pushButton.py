import sys
import time
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication,QWidget, QPushButton, QMenu

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPushButton")

        self.setGeometry(200,200, 500,400)

        btn =  QPushButton("Click me",self)

        btn.setGeometry(100,100,130,130)
        btn.setIcon(QIcon("icons/list.png"))
        btn.setIconSize(QSize(36,36))

        #btn.setFont(QFont("texgyre chorus"))

        #popup menu
        menu = QMenu()
        #menu.setFont(QFont("texgyre chorus"))
        #menu.setStyleSheet("background-color: yellow")

        menu.addAction("Copy")
        menu.addAction("Paste")
        menu.addAction("Cut")

        btn.setMenu(menu)

app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
