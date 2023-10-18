# not working... check later why

import sys
from PyQt6.QtWidgets import QApplication, QWidget

from PyQt6 import uic

class UI(QWidget):

    def __init_(self):
        super().__init__()

        uic.loadUi("untitled.ui",self)


app = QApplication(sys.argv)

window = UI()
window.show()

sys.exit(app.exec())
