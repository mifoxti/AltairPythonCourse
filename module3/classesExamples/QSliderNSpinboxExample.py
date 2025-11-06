import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QSlider, QSpinBox, QLabel, QPushButton)
from PyQt6.QtCore import Qt

from module1.stroki import message


class SliderSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.initUI()

    def initUI(self):
       self.setWindowTitle("QSlider + QSpinBox Demo - Ползунок и счетчик")
       self.setGeometry(300, 300, 400, 300)

       layout = QVBoxLayout()
       self.setLayout(layout)

       title = QLabel("🎚️ Настройки громкости: ")
       title.setStyleSheet("background-color: #4a3e69;"
                           "font-weight: bold;"
                           "font-size: 16px;"
                           "text-color: #cabbf0;"
                           "border-radius: 10px;")
       layout.addWidget(title)

       self.slider = QSlider(Qt.Orientation.Horizontal)
       self.slider.setRange(0, 100)
       self.slider.setValue(50)
       layout.addWidget(QLabel("Ползунок: "))
       layout.addWidget(self.slider)

       self.spinBox = QSpinBox()
       self.spinBox.setRange(0, 100)
       self.spinBox.setValue(50)
       layout.addWidget(QLabel("Счетчик: "))
       layout.addWidget(self.spinBox)

       self.slider.valueChanged.connect(self.spinBox.setValue)
       self.spinBox.valueChanged.connect(self.slider.setValue)

       apply_btn = QPushButton("🔊 Применить громкость")
       apply_btn.clicked.connect(self.apply_volume)
       layout.addWidget(apply_btn)

       self.result_label = QLabel("Громкость: 50%")
       self.result_label.setStyleSheet("background-color: #4a3e69;"
                           "font-weight: bold;"
                           "font-size: 16px;"
                           "text-color: #cabbf0;"
                           "border-radius: 10px;")
       layout.addWidget(self.result_label)

       self.slider.valueChanged.connect(self.update_result)

    def update_result(self, value):
        """Обновляет отображение громкости"""
        self.result_label.setText(f"Громкость: {value}%")
        if value < 30:
            color = "#c4f0b1"
        elif value < 60:
            color = "#ffd35c"
        else:
            color = "#ed021e"

        self.result_label.setStyleSheet(f"background-color: {color};"
                           "font-weight: bold;"
                           "font-size: 16px;"
                           "text-color: #cabbf0;"
                           "border-radius: 10px;")

    def apply_volume(self):
        """Применяет выбранную громкость"""
        volume = self.slider.value()

        if volume == 0:
            message = "🔇 Звук выключен"
        elif volume < 30:
            message = "🔈Тихо"
        elif volume < 60:
            message = "🔉 Нормально"
        else:
            message = "🔊 Громко"

        self.result_label.setText(f"{message}\nГромкость: {volume}%")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderSpinBoxDemo()
    window.show()
    sys.exit(app.exec())










