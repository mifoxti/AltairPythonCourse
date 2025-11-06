class Game:
    """Класс для управления игрой"""

    def __init__(self):
        self.pets = []  # Список всех питомцев
        self.day = 1

    def add_pets(self, pet):
        """Добавить питомца в игру"""
        self.pets.append(pet)
        print(f"{pet.name} успешно присоединился к игре!")

    def next_day(self):
        """Переход на следующий день"""
        self.day += 1
        print(f"\n{'=' * 30}")
        print(f"☀️ День {self.day}")
        print(f"\n{'=' * 30}")

        # У всех питомцев увеличивается голод и уменьшается счастье
        for pet in self.pets:
            pet.hunger += 10
            pet.happiness -= 5
            if hasattr(pet, "energy"):
                pet.energy -= 10
            if hasattr(pet, "magic_power"):
                pet.magic_power += 5

    def show_all_status(self):
        """Показывает статус всех наших питомцев"""
        print(f"\n📊 Статус всех питомце (День {self.day}):")
        for i, pet in enumerate(self.pets, 1):
            print(f"{i}. ", end="")
            pet.status()

    def interact_with_pet(self, pet_index):
        """Взаимодействие с конкретным питомцем"""
        if 0 <= pet_index < len(self.pets):
            pet = self.pets[pet_index]
            print(f"\n🎭 Взаимодействие с {pet.name}:")

            # Проверяем, какие действия доступны для этого питомца
            actions = ['Покормить', 'Узнать статус']

            if hasattr(pet, "fly"):
                actions.append('Полетать')
            if hasattr(pet, "fire_breath"):
                actions.append("Дыхнуть огнем")
            if hasattr(pet, "charge"):
                actions.append("Зарядить")

            # Показываем доступные действия
            for i, action in enumerate(actions, 1):
                print(f"{i}. {action}")

            # Здесь можно будет добавить функционал выбора действия
        else:
            print("❌ Питомец с таким номером не найден!")


game = Game()
from pets_library import DigitalPet, MagicDragon
from inheritance_example import RobotPet

game.add_pets(RobotPet("Вольт", "Surge"))
game.add_pets(MagicDragon('Сатир', 'фиолетовый'))
game.add_pets(DigitalPet("Курлык", "Попугай"))

game.show_all_status()
game.next_day()
game.show_all_status()

game.interact_with_pet(1)
