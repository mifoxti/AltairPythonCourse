class DigitalPet:

    #Конструктор - специальный метод, который вызывается при создании объекта
    def __init__(self, name, animal_type):
        # self - Это ссылка на сам объект. Как сказать "я" для питомца
        self.name = name
        self.animal_type = animal_type
        self.hunger = 50
        self.happiness = 50
        self.energy = 100

        print(f"Родился новый питомец! {self.name} - {self.animal_type}")

    # Методы - это действия, которые может выполнять питомец
    def feed(self):
        """Покормить питомца"""
        if self.hunger > 20:
            self.hunger -= 30
            self.happiness += 10
            print(f"{self.name} c удовольствием кушает!")
        else:
            print(f"{self.name} уже сыт!")

    def play(self):
        """Поиграть с питомцем"""
        if self.energy > 30:
            self.happiness += 20
            self.energy -= 25
            self.hunger += 15
            print(f"{self.name} весело играет!")
        else:
            print(f"{self.name} слишком устал дли игр")

    def sleep(self):
        """Уложить питомца спать"""
        self.energy = 100
        self.hunger += 20
        print(f"{self.name} сладко спит... zzz")

    def status(self):
        """Показать статус питомца"""
        print(f"\n--- Статус {self.name} ---")
        print(f"Голод: {self.hunger}/100")
        print(f"Счастье: {self.happiness}/100")
        print(f"Энергия: {self.energy}/100")


my_pet = DigitalPet("Барсик", "Аллигатор")
friends_pet = DigitalPet("Петра", "золотистый ретривер")

my_pet.status()
my_pet.feed()
my_pet.play()
friends_pet.status()


