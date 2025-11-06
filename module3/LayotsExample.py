import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QLineEdit)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Окно с макетами")
window.setGeometry(300, 300, 800, 800)


main_layout = QVBoxLayout()


title_label = QLabel("Расскажи о себе")
main_layout.addWidget(title_label)

name_layout = QHBoxLayout()
name_label = QLabel("Имя: ")
name_input = QLineEdit()
name_layout.addWidget(name_label)
name_layout.addWidget(name_input)

main_layout.addLayout(name_layout)

button = QPushButton("Представиться!")
main_layout.addWidget(button)

result = QLabel("Тут будет результат!")
main_layout.addWidget(result)

def on_button_clicked():
    name = name_input.text()
    if name:
        result.setText(f"Рад познакомиться, {name} 🦔")

button.clicked.connect(on_button_clicked)

window.setLayout(main_layout)
window.show()
app.exec()