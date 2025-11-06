import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QComboBox, QLabel, QPushButton)


class ComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("QComboBox Demo - Выпадающие списки")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("📕 Выбери свой любимый язык программирования")
        title.setStyleSheet("background-color: #3c423e;"
                            "text-color: white;"
                            "font-weight: bold;"
                            "font-size: 16px;"
                            "border-radius: 10px;")
        layout.addWidget(title)

        self.comboBox = QComboBox()

        languages = [
            "Python 🐍",
            "JavaScript 💛",
            "Java ☕",
            "C++ ⚡",
            "C# 🎮",
            "Kotlin 📱",
            "Swift 🐥"
        ]

        self.comboBox.addItems(languages)
        layout.addWidget(self.comboBox)

        select_button = QPushButton("✅ Выбрать")
        select_button.clicked.connect(self.show_selection)
        layout.addWidget(select_button)

        self.result = QLabel("Твой выбор появится здесь...")
        self.result.setStyleSheet("background-color: #3c423e;"
                            "text-color: white;"
                            "font-weight: bold;"
                            "font-size: 16px;"
                            "border-radius: 10px;")
        layout.addWidget(self.result)

    def show_selection(self):
        """Показывает выбранные элемент"""
        selected_language = self.comboBox.currentText()
        self.result.setText(f"💗 Отличный выбор!\nТы выбрал(а): {selected_language}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ComboBoxDemo()
    demo.show()
    sys.exit(app.exec())



