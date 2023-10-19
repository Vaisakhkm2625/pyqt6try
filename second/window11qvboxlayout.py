import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVHLayout")


        vbox = QVBoxLayout()
        

        button = []
        for i in range(5):
            btn = QPushButton(f"Click {i}",self)
            btn.move(100,i*100)
            vbox.addWidget(btn)
            button.append(btn)


        self.setLayout(vbox)
            




app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

