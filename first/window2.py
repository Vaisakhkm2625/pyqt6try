import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("Welcom PyQt6")

window.menuBar().addMenu("File")
#for i in range(10):
#    window.menuBar().addMenu("File"+str(i))

window.show()

sys.exit(app.exec())
