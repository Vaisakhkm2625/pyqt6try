import sys
from PyQt6.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayoutExample")

        grid = QGridLayout()


        rows = 5
        cols = 5

        buttonCol = []
        for i in range(cols):
            buttonRow = []
            for j in range(rows):
                btn = QPushButton()
                btn.setText(f"{i} {j}")
                buttonRow.append(btn)
            buttonCol.append(buttonRow)


        for i in range(cols):
            for j in range(rows):
                grid.addWidget(buttonCol[i][j],i,j)


        self.setLayout(grid)






app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
