import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit example")
        lineedit = QLineEdit(self)
        lineedit.setText("Default text")
        lineedit.setPlaceholderText("enter")
        #lineedit.setEnabled(False)
        lineedit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
