import random

secret = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Угадай число от 1 до 10: "))
    attempts += 1

    if guess == secret:
        print(f"Поздравляю! Ты угадал мое число за {attempts} попыток!")
        break
    elif guess < secret:
        print("Загаданное число больше!")
    else:
        print("Загаданное число меньше!")
else:
    print(f"Вы проиграли! Загаданное число было: {secret}")