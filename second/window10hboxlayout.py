import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout")


        hbox = QHBoxLayout()

        button = []
        for i in range(5):
            btn = QPushButton(f"click {i}",self)
            btn.move(100,i*100)
            button.append(btn)

        for btn in button:
            hbox.addWidget(btn)

        self.setLayout(hbox)








app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
