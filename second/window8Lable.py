import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont,QPixmap
from PyQt6.QtCore import QSize


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label example")


        label = QLabel("some text",self)
        label.setText("changed text")
        label.move(100,100)
        #label.setFont(QFont("texgyre chorus"))
        label.setStyleSheet("color:red")

        # adding image to label

        imgLabel = QLabel(self)
        pixmap = QPixmap("icons/list.png")
        label.setPixmap(pixmap)

        # movie for gifs


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())

