import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QSlider, QCheckBox,
    QSpinBox, QRadioButton, QButtonGroup, QProgressBar
)
from PyQt6.QtCore import Qt
import time


class SettingsApp(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.settings = {}
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        self.setWindowTitle("⚙️ Настройки приложения")
        self.setGeometry(200, 200, 500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("⚙️ Настройки приложения")
        title.setStyleSheet("font-size: 20px;"
                            "font-weight: bold;"
                            "color: #9c52c7;"
                            "margin: 10px;")
        layout.addWidget(title)

        # Раздел внешнего вида
        self.create_appearance_section(layout)

        # Раздел звука
        self.create_sound_section(layout)

        # Раздел управления
        self.create_controls_section(layout)

        # Раздел сохранения и загрузки
        self.create_action_buttons(layout)

        # Индикатор применения настроек
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

    def create_appearance_section(self, layout):
        """Раздел настроек внешнего вида"""
        section_label = QLabel("🎨 Внешний вид:")
        section_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(section_label)

        self.dark_theme = QCheckBox("🌙 Темная тема")
        layout.addWidget(self.dark_theme)

        # Выбор языка
        language_label = QLabel("🌐 Язык интерфейса:")
        layout.addWidget(language_label)
        self.language = QComboBox()
        self.language.addItems(["Russian", "English", "Spanish", "Chinese"])
        layout.addWidget(self.language)

        # Выбор размера шрифта
        font_label = QLabel("🔤 Размер шрифта:")
        layout.addWidget(font_label)

        # Создаем макет для радио-кнопок
        font_layout = QHBoxLayout()

        self.font_small = QRadioButton("Мелкий")
        self.font_medium = QRadioButton("Средний")
        self.font_large = QRadioButton("Большой")

        self.font_medium.setChecked(True)

        # Создаем группу для радио-кнопок (логическая группировка)
        font_group = QButtonGroup()
        font_group.addButton(self.font_small)
        font_group.addButton(self.font_medium)
        font_group.addButton(self.font_large)

        # Добавляем радио-кнопки в макет
        font_layout.addWidget(self.font_small)
        font_layout.addWidget(self.font_medium)
        font_layout.addWidget(self.font_large)

        # Добавляем макет в основной layout
        layout.addLayout(font_layout)

    def create_sound_section(self, layout):
        """Раздел настроек звука"""
        section_label = QLabel("🔊 Звук:")
        section_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(section_label)

        # Включить звук
        self.sound_enabled = QCheckBox("🔊 Включить звук")
        self.sound_enabled.setChecked(True)
        layout.addWidget(self.sound_enabled)

        # Громкость
        volume_label = QLabel("🎚️ Громкость:")
        layout.addWidget(volume_label)
        self.volume = QSlider(Qt.Orientation.Horizontal)
        self.volume.setRange(0, 100)
        self.volume.setValue(75)
        layout.addWidget(self.volume)

        # Отображение громкости
        self.volume_label = QLabel("75%")
        self.volume_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.volume_label)
        self.volume.valueChanged.connect(lambda v: self.volume_label.setText(f"{v}%"))

    def create_controls_section(self, layout):
        """Раздел настроек управления"""
        section_label = QLabel("🕹️ Управление:")
        section_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(section_label)

        # Скорость анимации
        speed_label = QLabel("⚡ Скорость анимации:")
        layout.addWidget(speed_label)
        self.animation_speed = QSpinBox()
        self.animation_speed.setRange(0, 10)
        self.animation_speed.setValue(5)
        layout.addWidget(self.animation_speed)

        # Дополнительные настройки
        self.auto_save = QCheckBox("💾 Автосохранение")
        self.auto_save.setChecked(True)
        layout.addWidget(self.auto_save)

        # Уведомления
        self.notifications = QCheckBox("🔔 Показывать уведомления")
        self.notifications.setChecked(True)
        layout.addWidget(self.notifications)

    def create_action_buttons(self, layout):
        """Кнопки действия"""
        buttons_layout = QHBoxLayout()

        # Сохранить настройки
        save_btn = QPushButton("💾 Сохранить настройки")
        save_btn.clicked.connect(self.save_settings)
        buttons_layout.addWidget(save_btn)

        # Сбросить настройки
        reset_btn = QPushButton("🗑️ Сбросить настройки")
        reset_btn.clicked.connect(self.reset_settings)
        buttons_layout.addWidget(reset_btn)

        # Показать настройки
        show_btn = QPushButton("👀 Показать настройки")
        show_btn.clicked.connect(self.show_settings)
        buttons_layout.addWidget(show_btn)

        # Добавляем макет с кнопками в основной layout
        layout.addLayout(buttons_layout)

    def save_settings(self):
        """Сохраняет настройки в файл"""
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        # Определяем размер шрифта
        font_size = "medium"
        if self.font_small.isChecked():
            font_size = "small"
        elif self.font_medium.isChecked():
            font_size = "medium"
        elif self.font_large.isChecked():
            font_size = "large"

        settings = {
            "theme": "dark" if self.dark_theme.isChecked() else "light",
            "language": self.language.currentText(),
            "font_size": font_size,
            "sound_enabled": self.sound_enabled.isChecked(),
            "volume": self.volume.value(),
            "animation_speed": self.animation_speed.value(),  # Исправлена опечатка
            "auto_save": self.auto_save.isChecked(),
            "notifications": self.notifications.isChecked(),
        }

        # Симуляция процесса сохранения
        for i in range(101):
            self.progress_bar.setValue(i)
            QApplication.processEvents()
            time.sleep(0.01)  # Исправлено: было 10 секунд (слишком долго)

        try:
            with open("settings.json", "w", encoding="utf-8") as settings_file:
                json.dump(settings, settings_file, ensure_ascii=False, indent=2)

            self.statusBar().showMessage("✅ Настройки сохранены успешно!")
        except Exception as e:
            self.statusBar().showMessage(f"❌ Ошибка: {str(e)}")

        self.progress_bar.setVisible(False)

    def load_settings(self):
        """Загружает настройки из файла"""
        try:
            with open("settings.json", "r", encoding="utf-8") as settings_file:
                settings = json.load(settings_file)

                # Применяем настройки
                self.dark_theme.setChecked(settings.get("theme", "light") == "dark")
                self.language.setCurrentText(settings.get("language", "Russian"))
                self.sound_enabled.setChecked(settings.get("sound_enabled", True))
                self.volume.setValue(settings.get("volume", 75))
                self.animation_speed.setValue(settings.get("animation_speed", 5))
                self.auto_save.setChecked(settings.get("auto_save", True))
                self.notifications.setChecked(settings.get("notifications", True))

                # Загружаем размер шрифта
                font_size = settings.get("font_size", "medium")
                if font_size == "small":
                    self.font_small.setChecked(True)
                elif font_size == "medium":
                    self.font_medium.setChecked(True)
                elif font_size == "large":
                    self.font_large.setChecked(True)

        except FileNotFoundError:
            # Файл настроек не существует - используем значения по умолчанию
            pass
        except Exception as e:
            print(f"Ошибка при загрузке настроек: {e}")

    def reset_settings(self):
        """Сбрасывает настройки к значениям по умолчанию"""
        self.dark_theme.setChecked(False)
        self.language.setCurrentText("Russian")
        self.sound_enabled.setChecked(True)
        self.volume.setValue(75)
        self.animation_speed.setValue(5)
        self.auto_save.setChecked(True)
        self.notifications.setChecked(True)
        self.font_medium.setChecked(True)  # Сбрасываем размер шрифта
        self.statusBar().showMessage("🔃 Настройки сброшены к значениям по умолчанию")

    def show_settings(self):
        """Показывает текущие настройки"""
        # Определяем размер шрифта
        font_size = "Средний"
        if self.font_small.isChecked():
            font_size = "Мелкий"
        elif self.font_medium.isChecked():
            font_size = "Средний"
        elif self.font_large.isChecked():
            font_size = "Большой"

        settings_text = f"""
📋 ТЕКУЩИЕ НАСТРОЙКИ:

🎨 Тема: {'Темная' if self.dark_theme.isChecked() else 'Светлая'}
🌐 Язык: {self.language.currentText()}
🔤 Размер шрифта: {font_size}
🔊 Звук: {'Включен' if self.sound_enabled.isChecked() else 'Выключен'}
🎚️ Громкость: {self.volume.value()}%
⚡ Скорость анимации: {self.animation_speed.value()}/10
💾 Автосохранение: {'Включено' if self.auto_save.isChecked() else 'Выключено'}
🔔 Уведомления: {'Включены' if self.notifications.isChecked() else 'Выключены'}
        """

        self.statusBar().showMessage("Настройки отображены в консоли!")
        print(settings_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsApp()
    window.show()
    sys.exit(app.exec())