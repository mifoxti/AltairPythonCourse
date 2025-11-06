import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Мое первое окно!")
window.setGeometry(300, 300, 400, 200)

window.show()

app.exec()