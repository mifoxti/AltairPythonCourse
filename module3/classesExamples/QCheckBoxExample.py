import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QCheckBox, QLabel, QPushButton,
                             QHBoxLayout)


class CheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("QCheckBox Demo - флажки выбора")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("Выбери свои интересы: ")
        title.setStyleSheet("font-size: 16px;"
                            "font-weight: bold;")
        layout.addWidget(title)

        self.checkbox_sports = QCheckBox("🏀 Спорт")
        self.checkbox_music = QCheckBox("🎵 Музыка")
        self.checkbox_books = QCheckBox("📕 Книги")
        self.checkbox_games = QCheckBox("🎮 Игры")
        self.checkbox_travel = QCheckBox("🛫 Путешествия")

        layout.addWidget(self.checkbox_sports)
        layout.addWidget(self.checkbox_music)
        layout.addWidget(self.checkbox_books)
        layout.addWidget(self.checkbox_games)
        layout.addWidget(self.checkbox_travel)

        show_btn = QPushButton("📊 Показать мой выбор")
        show_btn.clicked.connect(self.show_selection)
        layout.addWidget(show_btn)

        self.result_label = QLabel("Твой выбор появится тут...")
        self.result_label.setStyleSheet("background-color: #f0f8ff;"
                                        "padding: 10px;"
                                        "border-radius: 10px;")
        layout.addWidget(self.result_label)

    def show_selection(self):
        """Показывает выбранные флажки"""
        selected = []

        if self.checkbox_sports.isChecked():
            selected.append(self.checkbox_sports.text())
        if self.checkbox_music.isChecked():
            selected.append(self.checkbox_music.text())
        if self.checkbox_books.isChecked():
            selected.append(self.checkbox_books.text())
        if self.checkbox_games.isChecked():
            selected.append(self.checkbox_games.text())
        if self.checkbox_travel.isChecked():
            selected.append(self.checkbox_travel.text())

        if selected:
            result_text = "🎯 Твои интересы: \n" + "\n".join(selected)
        else:
            result_text = "😢 Ты ничего не выбрал(а)"

        self.result_label.setText(result_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CheckBoxDemo()
    demo.show()
    sys.exit(app.exec())
