import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QPushButton, QLineEdit)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Окно с полем для ввода!")
window.setGeometry(300, 300, 400, 300)

# Текст!
label = QLabel("Введи свое имя", window)
label.move(50, 50)

# Создадим для ввода
name_input = QLineEdit(window)
name_input.move(150, 150)
name_input.setPlaceholderText("Впиши имя сюда...")

# Кнопка
button = QPushButton("Поприветствовать", window)
button.move(150, 100)

# Текст результата
result_label = QLabel(window)
result_label.move(150, 200)
result_label.resize(200, 30)


def on_button_clicked():
    """теперь кнопка читает введенное имя"""
    name = name_input.text()
    if name:
        result_label.setText(f"Привет, {name}! 🖐️")
        result_label.adjustSize()
    else:
        result_label.setText(f"Ты еще не ввел имя :)")
        result_label.adjustSize()


button.clicked.connect(on_button_clicked)

window.show()
app.exec()
