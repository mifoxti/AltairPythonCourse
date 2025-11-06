total = 0
count = 0

print("Вводите числа (0 - завершение): ")
while True:
    number = float(input("Число: "))
    if number == 0:
        break

    total += number
    count += 1

if count > 0:
    print(f"Сумма: {total}")
    print(f"Количество чисел: {count}")
    print(f"Среднее арифметическое: {total / count}")
else:
    print("Вы не ввели ни одного числа! 😒")