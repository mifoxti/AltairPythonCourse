import sys
import time
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QProgressBar, QLabel, QPushButton, QSlider)
from PyQt6.QtCore import QTimer, Qt

class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("QProgressBar Demo - индикатор выполнения!")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("📊 Загрузка файла: ")
        title.setStyleSheet("border-radius: 10px;")
        layout.addWidget(title)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        layout.addWidget(QLabel("🎚️ Управление прогрессом"))
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.progress_bar.setValue)
        layout.addWidget(self.slider)

        buttons_layout = QVBoxLayout()

        start_btn = QPushButton("🚀 Начать загрузку")
        start_btn.clicked.connect(self.start_loading)
        buttons_layout.addWidget(start_btn)

        reset_btn = QPushButton("🚫 Сбросить")
        reset_btn.clicked.connect(self.reset_progress)
        buttons_layout.addWidget(reset_btn)

        layout.addLayout(buttons_layout)

        self.status_label = QLabel("Готов к загрузке...")
        self.status_label.setStyleSheet("border-radius: 10px;")
        layout.addWidget(self.status_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

    def start_loading(self):
        """Запускает автоматическую загрузку"""
        if not self.timer.isActive():
            self.progress_value = 0
            self.progress_bar.setValue(0)
            self.slider.setValue(0)
            self.timer.start(100) # каждые 100мс
            self.status_label.setText("📥 Загрузка началась...")

    def update_progress(self):
        """Обновлять прогресс загрузки"""
        self.progress_value += 2
        self.progress_bar.setValue(self.progress_value)
        self.slider.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.status_label.setText("✅ Загрузка завершена!")

    def reset_progress(self):
        """Сбрасывает прогресс"""
        self.timer.stop()
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.slider.setValue(0)
        self.status_label.setText("🔃 Прогресс сброшен, готов к загрузке!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBarDemo()
    window.show()
    sys.exit(app.exec())