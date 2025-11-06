import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Окно с текстом")
window.setGeometry(300, 300, 400, 300)

tittle_label = QLabel(window)
tittle_label.setText("Привет мир!")
tittle_label.move(150, 50)

subtitle_label = QLabel(window)
subtitle_label.setText("Я изучаю PyQt6")
subtitle_label.move(140, 80)

window.show()
app.exec()