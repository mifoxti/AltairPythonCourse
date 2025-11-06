import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QLabel,
                             QPushButton, QLineEdit)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Красивое окно!")
window.setGeometry(300, 300, 400, 400)

window.setStyleSheet("""
    background-color: #f0f8ff;
    font-family: Arial;
""")

layout = QVBoxLayout()

title_label = QLabel("Мое красивое приложение")
title_label.setStyleSheet("""
    font-size: 20px;
    font-wight: bold;
    color: #2e86ab;
    padding: 10px;
    border-radius: 10px;
""")
layout.addWidget(title_label)

name_input = QLineEdit(window)
name_input.setPlaceholderText("Введи свое имя!")
name_input.setStyleSheet("""
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 10px;
    font-size: 14px;
""")
layout.addWidget(name_input)

button = QPushButton("Нажми на меня!")
button.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 10px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
""")
layout.addWidget(button)

result_label = QLabel("Жду твоего имени...")
result_label.setStyleSheet("""
    font-size: 16px;
    color: #333;
    padding: 10px;
    background-color: #e8f4f8;
    border-radius: 10px;
""")
layout.addWidget(result_label)


def on_button_clicked():
    name = name_input.text()
    if name:
        result_label.setText(f"Привет, {name}! Ты отлично выглядишь! ❤️")


button.clicked.connect(on_button_clicked)

window.setLayout(layout)
window.show()
app.exec()
