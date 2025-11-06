# НЕПРАВИЛЬНО
# x = 1
# while x > 0:
#     print(x)
#     x = x + 1

# ПРАВИЛЬНО

# x = 1
# while x <= 10:
#     print(x)
#     x += 1

# НЕПРАВИЛЬНО
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num) # Опасно!

# НЕПРАВИЛЬНО
counter = 0
while counter < 10:
    print(counter)
    # Забыл прописать counter += 1
    