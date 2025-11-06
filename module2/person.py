class Person:
    """
    Класс для демонстрации конструкторов и инициализации.
    Показывает разницу между обычными методами и методами класса
    """

    # Атрибут класса - общий для всех экземпляров
    species = "Homo Sapiens"
    population = 0

    def __init__(self, name, age, email=None):
        """
        Основной конструктор.
        Вызывается автоматически при создании объекта: Person("Иван", 25)
        """
        # Атрибуты экземпляра - уникальные для каждого объекта
        self.name = name
        self.age = age
        self.email = email
        self._internal_id = self._generate_id()  # Защищенный атрибут

        # Изменяем атрибут класса
        Person.population += 1

    def _generate_id(self):
        """Защищенный метод для генерации внутреннего ID"""
        return f"P{id(self) % 10000:04d}"

    @classmethod
    def from_birth_year(cls, name, birth_year, email=None):
        """
        Фабричный метод класса.
        Создает объект на основе года рождения вместо возраста.
        cls - это ссылка на сам класс (аналог self для методов класса
        """
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age, email)  # Вызываем основной конструктор

    @classmethod
    def from_dict(cls, data_dict):
        """
        Еще один фабричный метод - создает объект из словаря.
        Полезно при работе с JSON данными.
        """
        return cls(
            name=data_dict.get("name"),
            age=data_dict.get("age"),
            email=data_dict.get("email")
        )

    @classmethod
    def get_population(cls):
        """Метод класса - работает с атрибутами класса"""
        return f"Всего людей на планете: {cls.population}"

    @staticmethod
    def is_adult(age):
        """
        Статический метод - не требует доступа к self или cls
        Просто функция, логически связанная с классом
        """
        return age >= 18

    def __str__(self):
        return f"Person: {self.name}, age: {self.age}, ID: {self._internal_id}"


print("=== Разные конструкторы ===")

# Обычный конструктор
person1 = Person("Анна", 19, "anna@gmail.com")
print(person1)

# Фабричный метод - из года рождения
person2 = Person.from_birth_year("Дарья", 2003)
print(person2)

# Фабричный метод из словаря
person_data = {'name': "Тимофей", 'age': 21, "email": "microfoxti@gmail.com"}
person3 = Person.from_dict(person_data)
print(person3)

print(f"\n{Person.get_population()}")

# Статический метод - можно вызвать без создания объекта
print(f"18 лет - взрослый: {Person.is_adult(18)}")
print(f"15 лет - взрослый: {Person.is_adult(15)}")
