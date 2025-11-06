class Configuration:
    """
    Демонстрация атрибутов класса и экземпляров.
    Атрибуты класса полезны для констант и общих данных
    """

    # Атрибуты класса - общие для всех экземпляров
    APP_NAME = "TikTok"
    VERSION = "1.0.0"
    MAX_USERS = 1000
    instances_created = 0

    def __init__(self, env, debug=False):
        # Атрибуты экземпляра - уникальные для каждого объекта
        self.env = env
        self.debug = debug
        self._settings = {}

        # Изменяем атрибут класса
        Configuration.instances_created += 1

    def set_settings(self, key, value):
        """Устанавливает настройку для этого конкретного экземпляра"""
        self._settings[key] = value

    def get_settings(self, key):
        """Получает настройку для этого конкретного экземпляра"""
        return self._settings.get(key)

    @classmethod
    def get_app_info(cls):
        """Метод класса - работает только с атрибутами класса"""
        return f"{cls.APP_NAME} v{cls.VERSION}, макс. пользователей: {cls.MAX_USERS}"

    @classmethod
    def get_instances_count(cls):
        return f"Создано конфигураций приложения: {cls.instances_created}"

    def get_instance_info(self):
        """Метод экземпляра - работает с атрибутами экземпляра и класса"""
        return f"Среда: {self.env}, debug: {self.debug}, Приложение: {self.APP_NAME}"


# Демонстрация работы с атрибутами
print("=== Атрибуты класса и экземпляра ===")

# Создаем несколько объектов
dev_config = Configuration("development", debug=True)
prod_config = Configuration("production", debug=False)

# Устанавливаем разные настройки для каждого экземпляра
dev_config.set_settings("database", "sqlite:///:memory:")
prod_config.set_settings("database", "postgresql:///:prod_server:")

print(dev_config.get_instance_info())
print(f"Настройки dev: {dev_config.get_settings('database')}")

print(prod_config.get_instance_info())
print(f"Настройки prod: {prod_config.get_settings('database')}")

# Атрибуты класса доступны через класс и через экземпляры
print(f"\nЧерез класс: {Configuration.APP_NAME}")
print(f"Через экземпляр: {dev_config.APP_NAME}")

# Изменяем атрибут, видим, что изменения коснулись всех экземпляров
Configuration.VERSION = "1.1.0"
print(f"После изменения: {dev_config.VERSION}, {prod_config.VERSION}")

print(Configuration.get_instances_count())
print(Configuration.get_app_info())
