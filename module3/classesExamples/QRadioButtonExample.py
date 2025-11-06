import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QButtonGroup,
                             QRadioButton, QLabel, QPushButton)

from module2.homework_analog.validate_email import message


class RadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton Demo - Переключатели")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("🔘 Выбери свою возрастную группу:")
        title.setStyleSheet("border-radius: 10px;")
        layout.addWidget(title)

        self.radio_teen = QRadioButton("👶 13-17 лет")
        self.radio_young = QRadioButton("👩‍🦱 18-25 лет")
        self.radio_adult = QRadioButton("👨‍🦰 26-40 лет")
        self.radio_senior = QRadioButton("🧓 41+ лет")

        layout.addWidget(self.radio_teen)
        layout.addWidget(self.radio_young)
        layout.addWidget(self.radio_adult)
        layout.addWidget(self.radio_senior)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_teen)
        self.button_group.addButton(self.radio_young)
        self.button_group.addButton(self.radio_adult)
        self.button_group.addButton(self.radio_senior)

        select_btn = QPushButton("✅ Подтвердить выбор!")
        select_btn.clicked.connect(self.show_selection)
        layout.addWidget(select_btn)

        self.result_label = QLabel("Выбери вариант выше...")
        self.result_label.setStyleSheet("border-radius: 10px;")
        layout.addWidget(self.result_label)

    def show_selection(self):
        """Показывает выбранный переключатель"""
        if self.radio_teen.isChecked():
            message = "👶 Ты подросток! учись и развивайся, у тебя все впереди!"
        elif self.radio_young.isChecked():
            message = "👩‍🦱 Молодость - время возможностей!"
        elif self.radio_adult.isChecked():
            message = "👨‍🦰 Взрослая жизнь - время достижений!"
        else:
            message = "🧓 Опыт - он как вино, с годами только лучше!"

        self.result_label.setText(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = RadioButtonDemo()
    demo.show()
    sys.exit(app.exec())
