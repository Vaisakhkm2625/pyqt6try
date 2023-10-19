import sys
from PyQt6.QtWidgets import QApplication, QLabel,QWidget,QLabel, QVBoxLayout,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Event handling")

        self.vbox = QVBoxLayout()

        btn = QPushButton("change text")
        btn.clicked.connect(self.change_text)

        self.label = QLabel("Hello")

        self.vbox.addWidget(btn)
        self.vbox.addWidget(self.label)


        self.setLayout(self.vbox)


    def change_text(self):
        self.label.setText("text setted")

        btn = QPushButton("new button")
        self.vbox.addWidget(btn)






app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())
