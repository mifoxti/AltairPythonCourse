# while условие:
#     # блок кода, который повторяется
#     действия


while True:
    print('''1 - Сложить\n2 - Выйти''')
    choice = int(input("Выберите действие: "))
    if choice == 2:
        print('До свидания!!!')
        break

    if choice == 1:
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))
        print(f"Результат: {a + b}")
        

