

# for переменная in последовательность:
#     # блок кода, который повторяться
#     действия


# range(5) создает последовательность: 0, 1, 2, 3, 4
# for i in range(5):
#     print(f"Номер итерации: {i}")

# range(stop)   # 0, 1, 2, 3 ... stop - 1
# range(start, stop)     # start, start + 1, start + 2, ... stop - 1
# range(start, stop, step)   #start, start + step, start + step * 2, ... stop - 1

# print("range(3):")
# for i in range(3):
#     print(i) # 0, 1, 2
#
# print("range(1, 4):")
# for i in range(1, 4):
#     print(i) # 1, 2, 3
#
# print("range(0, 10, 2):")
# for i in range(0, 10, 2):
#     print(i) # 0, 2, 4, 6, 8
#
# print("range(5, 0, -1):")
# for i in range(5, 0, -1):
#     print(i) # 5, 4, 3, 2, 1

# Перебор строки (по символам)
# word = "Python"
# for letter in word:
#     print(letter)


# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"I like №{index} {fruit}")

# sum = 0
# for i in range(1, 6): # 1, 2, 3, 4, 5
#     sum += i
#     print(f"После {i} итерации сумма = {sum}")
# print(f"Итоговая сумма: {sum}")

num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")