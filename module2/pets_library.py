class DigitalPet:
    """Базовый класс для всех цифровых питомцев"""

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 50
        self.happiness = 50
        self.energy = 100

    def feed(self):
        """Покормить питомца"""
        if self.hunger > 20:
            self.hunger -= 30
            self.happiness += 10
            print(f"{self.name} c удовольствием кушает!")
        else:
            print(f"{self.name} уже сыт!")

    def status(self):
        """Показать статус питомца"""
        print(f"\n--- Статус {self.name} {self.animal_type} ---")
        print(f"Голод: {self.hunger}/100")
        print(f"Счастье: {self.happiness}/100")
        print(f"Энергия: {self.energy}/100")

class MagicDragon(DigitalPet):  # В скобках указываем родительский класс
    """Волшебный дракон - умеет летать и дышать огнем"""

    def __init__(self, name, color):
        # super() обращается к родительскому классу
        super().__init__(name, "Волшебный дракон")
        self.color = color  # Новое свойства - цвет дракона
        self.magic_power = 100  # Новое свойство - магическая сила

    # Новый метод, которого нет у обычных питомцев
    def fly(self):
        """Дракон умеет летать!"""
        if self.energy > 40:
            self.energy -= 30
            print(f"{self.name} взлетает в небо! Его {self.color} чешуя блестит на солнце!")
        else:
            print(f"{self.name} слишком устал и ленится летать!")

    def fire_breath(self):
        """Дракон дышит огнем"""
        if self.magic_power > 20:
            self.magic_power -= 15
            print(f"{self.name} извергает пламя! Боже, как же жарко!")
        else:
            print(f"У {self.name} не хватает маны, нужно закупить больше маны!")