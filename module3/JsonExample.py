import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QLabel,
                             QPushButton, QLineEdit, QTextEdit, QHBoxLayout)
import datetime

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Дневник настроения")
window.setGeometry(300, 300, 500, 400)

layout = QVBoxLayout()

title = QLabel("Как твое настроение?")
title.setStyleSheet("font-size: 18px;"
                    "font-weight: bold;")
layout.addWidget(title)

name_input = QLineEdit()
name_input.setPlaceholderText("Твое имя")
layout.addWidget(name_input)

mood_input = QLineEdit()
mood_input.setPlaceholderText("Опиши свое настроение!")
mood_input.setStyleSheet("""
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 10px;
    font-size: 14px;
""")
layout.addWidget(mood_input)

h_layout = QHBoxLayout()

save_button = QPushButton("💾 Сохранить настроение!")
save_button.setStyleSheet("""
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
h_layout.addWidget(save_button)
load_button = QPushButton("📖 Загрузить историю")
load_button.setStyleSheet("""
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
h_layout.addWidget(load_button)
layout.addLayout(h_layout)

history_display = QTextEdit()
history_display.setReadOnly(True)
layout.addWidget(history_display)


def save_mood():
    """Сохраняем наше настроение"""
    name = name_input.text()
    mood = mood_input.text()

    if not name or not mood:
        history_display.setText("Вы еще не ввели имя и настроение!")
        return

    mood = {
        'name': name,
        'mood': mood,
        'timestamp': datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    }

    try:
        # Попытаемся прочитать существующие данные
        if os.path.exists('moods.json'):
            with open("moods.json", 'r', encoding='utf-8') as f:
                all_moods = json.load(f)  # Читаем данные из файла
        else:
            all_moods = []

        all_moods.append(mood)

        # Сохраняем данные обратно в файл
        with open("moods.json", "w", encoding='utf-8') as f:
            json.dump(all_moods, f, ensure_ascii=False, indent=2)
            # ensure_ascii = False - сохраняет русски буквы
            # indent = 2 - красивые отступы

        history_display.setText(f"✅ Настроение {name} сохранено!\nВсего записей: {len(all_moods)}")

        name_input.clear()
        mood_input.clear()
    except Exception as e:
        history_display.setText(f"❌ Ошибка: {str(e)}")


def load_history():
    """Загружать историю настроений из файла"""
    try:
        if os.path.exists('moods.json'):
            with open("moods.json", "r", encoding='utf-8') as f:
                moods = json.load(f)

                # Формируем красивый текст!
                history_text = "📔 ИСТОРИЯ НАСТРОЕНИЙ: \n\n"
                for mood in moods:
                    history_text += f"👤 {mood['name']} ({mood['timestamp']}): {mood['mood']}\n"

                history_display.setText(history_text)
        else:
            history_display.setText("История пуста, сохрани свое первое настроение!")
    except json.JSONDecodeError as e:
        history_display.setText(f"❌Файл с историей поврежден! {str(e)}")
    except Exception as e:
        history_display.setText(f"❌Ошибка: {str(e)}")


# Подключаем кнопки
save_button.clicked.connect(save_mood)
load_button.clicked.connect(load_history)

window.setLayout(layout)
window.show()
app.exec()
