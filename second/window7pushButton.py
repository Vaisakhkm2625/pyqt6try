import sys
from PyQt6.QtWidgets import QApplication,QWidget, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPushButton")

        self.setGeometry(200,200, 500,400)

        btn =  QPushButton("Click me",self)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
