import sys
from PyQt6.QtWidgets import QApplication, QWidget

from designerwindow_ui import Ui_Form


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("title")

app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())
 
