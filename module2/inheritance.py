class Vehicle:
    """Класс базового транспортного средства"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._engine_started = False
        self.__vin = self.__generate_vin() # Приватный атрибут

    def __generate_vin(self):
        """Приватный метод генерации VIN"""
        return f"VIN{id(self) % 100000:05d}"

    def start_engine(self):
        """Запуск двигателя - общий для всех транспортных средств"""
        self._engine_started = True
        return f"Двигатель {self.brand} {self.model} запущен"

    def stop_engine(self):
        """Остановка двигателя"""
        self._engine_started = False
        return f"Двигатель {self.brand} {self.model} заглушен"

    def _get_vehicle_info(self):
        """Защищенгный метод - внутренняя информация"""
        return f"{self.brand} {self.model} {self.year}"


class Car(Vehicle):
    """Класс Автомобиль - наследуется от Vehicle"""

    def __init__(self, brand, model, year, fuel_type, doors=4):
        # super() - обращение к родительскому классу
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = doors
        self.__car_specific_data = "Секретные данные автомобиля" # Свой приватный атрибут

    # Переопределим метод родительского класса
    def start_engine(self):
        """Специфический запуск автомобиля"""
        result = super().start_engine()
        return f"🚗 {result}. Автомобиль готов к поездке!"

    # Новый метод, специфичный для автомобиля
    def honk(self):
        return "Beep beep!"

    def get_car_info(self):
        """Метод, использующий защищенный метод родителя"""
        base_info = self._get_vehicle_info() # Доступ к защищенному методу
        return f"{base_info}, Тип топлива: {self.fuel_type}, Двери {self.doors}"


class ElectricCar(Car):
    """Класс Электромобиль - наследует класс Car (многоуровневое наследование)"""

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, "Электричесвто", 4)
        self.battery_capacity = battery_capacity
        self.__batery_health = 100 # Приватный атрибут электромобиля


    def start_engine(self):
        """Переопределение для автомобиля"""
        self._engine_started = True
        return f"🔋 {self.brand} {self.model}: Электродвигатель активирован!"

    def charge_battery(self):
        """Уникальный метод электромобиля"""
        return "⚡ Заряжаем батарею"


# использование наследования
print('=== Базовый класс ===')
vehicle = Vehicle("Generic", "Transport", 2020)
print(vehicle.start_engine())

print('\n=== Наследник Car ===')
car = Car("Toyota", "Camry 3.5", 2022, "бензин", 4)
print(car.start_engine())
print(car.honk())
print(car.get_car_info())

print('\n=== Многоуровневое наследование ===')
tesla = ElectricCar("Tesla", "Model X", 2023, 100)
print(tesla.start_engine())
print(tesla.honk())
print(tesla.charge_battery())
print(tesla.get_car_info())