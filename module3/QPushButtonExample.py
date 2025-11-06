import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Окно с кнопкой")
window.setGeometry(300, 300, 400, 300)

# Текст
title_label = QLabel(window)
title_label.setText("Нажми на кнопку!")
title_label.move(150, 50)

def on_button_clicked():
    """Функция, которая выполняется при нажатии кнопки"""
    title_label.setText("Ура! Кнопка работает! 👌")
    title_label.adjustSize()

# Добавим кнопку
button = QPushButton(window)
button.setText("Нажми меня!")
button.move(150, 100)
button.clicked.connect(on_button_clicked)

window.show()
app.exec()