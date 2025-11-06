"""Основная программа - импортируем питомцев"""

# Способ 1: Импорт всего модуля
# import pets_library
#
# dragon1 = pets_library.MagicDragon("Дуриан", "Черно-красный")
# dragon1.fly()

# Способ 2: Импорт конкретного класса
# from pets_library import DigitalPet, MagicDragon
# dragon = MagicDragon("Саурон", "Темно-лотой")
# pup = DigitalPet("Бетси", "Овчарка")

# Способ 3: Импорт всего из определенного файла (Не рекомендуется, но возможно)
from pets_library import *


dragon3 = MagicDragon("Аметист", "красный")
dragon3.status()
