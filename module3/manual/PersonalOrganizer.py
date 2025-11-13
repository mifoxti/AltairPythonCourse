import sys
import json
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox,
    QComboBox, QSlider, QSpinBox, QProgressBar, QRadioButton,
    QButtonGroup, QListWidget, QDateEdit
)
from PyQt6.QtCore import QDate, Qt


class PersonalOrganizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("📅 Персональный органайзер")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Левая панель - добавление задач
        left_panel = self.create_task_creation_panel()
        main_layout.addWidget(left_panel)

        # Правая панель - управление и отображение
        right_panel = self.create_task_management_panel()
        main_layout.addWidget(right_panel)

    def create_task_creation_panel(self):
        panel = QWidget()
        panel.setMaximumWidth(350)
        layout = QVBoxLayout()

        # QLabel - заголовок
        title = QLabel("➕ Новая задача")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E86AB;")
        layout.addWidget(title)

        # QLineEdit - название задачи
        self.task_title = QLineEdit()
        self.task_title.setPlaceholderText("Название задачи...")
        layout.addWidget(QLabel("Название:"))
        layout.addWidget(self.task_title)

        # QTextEdit - описание
        self.task_description = QTextEdit()
        self.task_description.setMaximumHeight(80)
        self.task_description.setPlaceholderText("Описание задачи...")
        layout.addWidget(QLabel("Описание:"))
        layout.addWidget(self.task_description)

        # QDateEdit - дата выполнения
        self.task_date = QDateEdit()
        self.task_date.setDate(QDate.currentDate())
        self.task_date.setCalendarPopup(True)
        layout.addWidget(QLabel("Дата выполнения:"))
        layout.addWidget(self.task_date)

        # QComboBox - категория
        self.task_category = QComboBox()
        self.task_category.addItems(["Работа", "Личное", "Учеба", "Здоровье", "Другое"])
        layout.addWidget(QLabel("Категория:"))
        layout.addWidget(self.task_category)

        # QSlider - приоритет
        priority_layout = QHBoxLayout()
        priority_layout.addWidget(QLabel("Приоритет:"))
        self.task_priority = QSlider(Qt.Orientation.Horizontal)
        self.task_priority.setRange(1, 5)
        self.task_priority.setValue(3)
        priority_layout.addWidget(self.task_priority)
        self.priority_label = QLabel("3/5")
        priority_layout.addWidget(self.priority_label)
        layout.addLayout(priority_layout)
        self.task_priority.valueChanged.connect(
            lambda v: self.priority_label.setText(f"{v}/5")
        )

        # QCheckBox - срочная задача
        self.task_urgent = QCheckBox("🚨 Срочная задача")
        layout.addWidget(self.task_urgent)

        # QSpinBox - estimated time
        self.task_estimated = QSpinBox()
        self.task_estimated.setRange(15, 480)
        self.task_estimated.setSuffix(" минут")
        self.task_estimated.setValue(60)
        layout.addWidget(QLabel("Примерное время:"))
        layout.addWidget(self.task_estimated)

        # QPushButton - добавить задачу
        add_btn = QPushButton("✅ Добавить задачу")
        add_btn.clicked.connect(self.add_task)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(add_btn)

        # QProgressBar - прогресс дня
        self.daily_progress = QProgressBar()
        self.daily_progress.setValue(0)
        layout.addWidget(QLabel("Прогресс дня:"))
        layout.addWidget(self.daily_progress)

        panel.setLayout(layout)
        return panel

    def create_task_management_panel(self):
        panel = QWidget()
        layout = QVBoxLayout()

        # QLabel - заголовок
        title = QLabel("📋 Мои задачи")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E86AB;")
        layout.addWidget(title)

        # QListWidget - список задач
        self.tasks_list = QListWidget()
        layout.addWidget(self.tasks_list)

        # Радио-кнопки для фильтрации
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Фильтр:"))

        self.filter_group = QButtonGroup()
        self.filter_all = QRadioButton("Все")
        self.filter_pending = QRadioButton("Активные")
        self.filter_completed = QRadioButton("Выполненные")

        self.filter_all.setChecked(True)

        for radio in [self.filter_all, self.filter_pending, self.filter_completed]:
            self.filter_group.addButton(radio)
            filter_layout.addWidget(radio)
            radio.toggled.connect(self.update_task_list)

        layout.addLayout(filter_layout)

        # Кнопки управления
        buttons_layout = QHBoxLayout()

        complete_btn = QPushButton("✅ Выполнено")
        complete_btn.clicked.connect(self.complete_task)
        buttons_layout.addWidget(complete_btn)

        delete_btn = QPushButton("🗑️ Удалить")
        delete_btn.clicked.connect(self.delete_task)
        buttons_layout.addWidget(delete_btn)

        edit_btn = QPushButton("✏️ Редактировать")
        edit_btn.clicked.connect(self.edit_task)
        buttons_layout.addWidget(edit_btn)

        layout.addLayout(buttons_layout)

        # Статистика
        stats_layout = QHBoxLayout()

        self.stats_total = QLabel("Всего: 0")
        self.stats_completed = QLabel("Выполнено: 0")
        self.stats_urgent = QLabel("Срочных: 0")

        for stat in [self.stats_total, self.stats_completed, self.stats_urgent]:
            stat.setStyleSheet("background-color: #f0f8ff; padding: 5px; border-radius: 3px;")
            stats_layout.addWidget(stat)

        layout.addLayout(stats_layout)

        panel.setLayout(layout)
        return panel

    def add_task(self):
        title = self.task_title.text().strip()
        if not title:
            return

        task = {
            "title": title,
            "description": self.task_description.toPlainText(),
            "date": self.task_date.date().toString("dd.MM.yyyy"),
            "category": self.task_category.currentText(),
            "priority": self.task_priority.value(),
            "urgent": self.task_urgent.isChecked(),
            "estimated": self.task_estimated.value(),
            "completed": False,
            "created": datetime.now().strftime("%d.%m.%Y %H:%M")
        }

        self.tasks.append(task)
        self.update_task_list()
        self.update_statistics()

        # Очистка формы
        self.task_title.clear()
        self.task_description.clear()
        self.task_priority.setValue(3)
        self.task_urgent.setChecked(False)
        self.task_estimated.setValue(60)

    def update_task_list(self):
        self.tasks_list.clear()

        for i, task in enumerate(self.tasks):
            if self.filter_pending.isChecked() and task["completed"]:
                continue
            if self.filter_completed.isChecked() and not task["completed"]:
                continue

            status = "✅" if task["completed"] else "⏳"
            urgent = "🚨" if task["urgent"] else ""
            text = f"{status} {urgent} [{task['category']}] {task['title']} (Приоритет: {task['priority']}/5)"

            if task["completed"]:
                text = f"<s>{text}</s>"

            self.tasks_list.addItem(text)

    def update_statistics(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        urgent = sum(1 for t in self.tasks if t["urgent"])

        self.stats_total.setText(f"Всего: {total}")
        self.stats_completed.setText(f"Выполнено: {completed}")
        self.stats_urgent.setText(f"Срочных: {urgent}")

        # Обновляем прогресс
        progress = int((completed / total) * 100) if total > 0 else 0
        self.daily_progress.setValue(progress)

    def complete_task(self):
        current_row = self.tasks_list.currentRow()
        if current_row >= 0:
            # Находим задачу в отфильтрованном списке
            filtered_tasks = self.get_filtered_tasks()
            if current_row < len(filtered_tasks):
                task = filtered_tasks[current_row]
                task["completed"] = True
                self.update_task_list()
                self.update_statistics()

    def delete_task(self):
        current_row = self.tasks_list.currentRow()
        if current_row >= 0:
            filtered_tasks = self.get_filtered_tasks()
            if current_row < len(filtered_tasks):
                task = filtered_tasks[current_row]
                self.tasks.remove(task)
                self.update_task_list()
                self.update_statistics()

    def edit_task(self):
        current_row = self.tasks_list.currentRow()
        if current_row >= 0:
            filtered_tasks = self.get_filtered_tasks()
            if current_row < len(filtered_tasks):
                task = filtered_tasks[current_row]
                # Здесь можно реализовать редактирование задачи
                print(f"Редактирование: {task['title']}")

    def get_filtered_tasks(self):
        if self.filter_pending.isChecked():
            return [t for t in self.tasks if not t["completed"]]
        elif self.filter_completed.isChecked():
            return [t for t in self.tasks if t["completed"]]
        else:
            return self.tasks


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonalOrganizer()
    window.show()
    sys.exit(app.exec())
