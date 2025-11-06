# break - немедленный выход из цикла
from re import search

# numbers = [1, 3, 7, 5, 9, 8]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"Наконец-то мы его нашли, число которое делится на 2: {num}")
#         break
#     print(f"Проверяес {num} - нечетное")

# continue - переход к следующей итерации

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
serch = int(input("Какое число мы хотим найти? "))

for num in numbers:
    if num == serch:
        print(f"Число {serch} найдено! Его индекс - {numbers.index(num)}")
        break
else:
    print(f"Число {serch} не найдено в списке!")