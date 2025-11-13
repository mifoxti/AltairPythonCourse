import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QRadioButton, QButtonGroup, QLabel)


class RadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("QRadioButton Demo")
        layout = QVBoxLayout()

        self.button_group = QButtonGroup()

        # Создаем переключатели
        self.radio1 = QRadioButton("Вариант 1")
        self.radio2 = QRadioButton("Вариант 2")
        self.radio3 = QRadioButton("Вариант 3")

        # Добавляем в группу
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.button_group.addButton(self.radio3)

        # Подключаем сигналы
        self.radio1.toggled.connect(self.on_radio_toggled)
        self.radio2.toggled.connect(self.on_radio_toggled)
        self.radio3.toggled.connect(self.on_radio_toggled)

        # Добавляем в layout
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        self.label = QLabel("Выберите вариант")
        layout.addWidget(self.label)

        self.setLayout(layout)

    def on_radio_toggled(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(f"Выбран: {radio.text()}")


app = QApplication(sys.argv)
window = RadioButtonDemo()
window.show()
app.exec()