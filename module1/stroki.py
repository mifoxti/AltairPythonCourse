print("a" + "b" * 2)





text1 = 'Простая строка'
text2 = 'Строка с "кавычками" внутри'

text3 = "Простая строка"
text4 = "Строка с 'кавычками' внутри"
long_text = '''Это очень длинный текст,
который занимает несколько строк
и при этом сохраняет переносы строк!'''

# С помощью обратного слэша \
text = "Он сказал: \"Привет!\""
path = "C:\\Users\\Timofey\\Docunets\\Altair\\Urok.mp4"
new_line = "Первая строка\nВторая строка"
tab_text = "Колонка1\tКолонка2"


# print(text)
# print(path)
# print(new_line)
# print(tab_text)

# Сырые строки игнорируют экранирование
# path = r"D:\brogramming\nltair\.venv\tcripts\python.exe"
# print(path)

firts_name = "John"
second_name = "Smith"
full_name = firts_name + " " + second_name
# print(full_name)

line = "-" * 20
hello = "Hello" * 3
# print(line)
# print(hello)

text = "Hello World"
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[-1])
# print(text[-2])

# print(text[0:5]) # Hello (от 0 до 4)
# print(text[6:11]) # World (от 6 до 10)
# print(text[3:]) # lo World (от 3 до конца)
# print(text[:5]) # Hello (от начала до 4)
# print(text[::2]) # HloWrd (каждый второй символ)
# print(text[::-1]) #dlroW olleH (реверс строки)

# РЕГИСТР СИМВОЛОВ
text = "Hello World. Im timofey!"

# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# print(text.swapcase())

# Поиск и замена

text = "Я изучаю Python и Python это круто"

# print(text.find("Python")) # Первое вхождение (индекс первого символа)
# print(text.rfind("Python")) # Последние вхождение (индекс первого символа)
# print(text.find("Timofey")) # -1 Значит, что не найдено
# print(text.index("Python")) # Аналогично find, но ошибка, если нет
# print(text.count("Python")) # Сколько раз нашлось переданное

new_text = text.replace("Python", "Kotlin")
# print(new_text)

new_text = text.replace("Python", "C++", 1)
# print(new_text)

# Проверка содержимого
text1 = "Hello123"
text2 = "HELLO"
text3 = "hello"
text4 = '123'
text5 = "     "
text6 = 'Hello World'

# print(text1.isalnum()) # Проверка на буквы и цифры
# print(text1.isalpha()) # Проверка на исключительно буквы
# print(text2.isdigit()) # Проверка на исключительно цифры
# print(text2.isupper()) # Проверка, что все символы в верхнем регистре
# print(text3.islower()) # Проверка на то, что все символы в нижнем регистре
# print(text5.isspace()) # Проверка на то, что все символы - пробельные
# print(text6.istitle()) # Проверка на то, что все слова с заглавной буквы
# print(text1.startswith('Hello')) # Проверка на начало с комбинации
# print(text1.endswith('123')) # Проверка на окончание с комбинацией

# Разделение и соединение
text = "apple,banana,cherry,orange"
massive = ['apple', 'banana', 'cherry', 'orange']

# Разделение строки
fruits = text.split(',')
# print(fruits == massive)

text = "apple banana cherry orange"
fruits = text.split()
# print(fruits)

# Ограничение количества разбиений
text = "apple banana cherry orange"
fruits = text.split(' ', 2)
# print(fruits)

# Соединение строк
joint_fuits = ", ".join(fruits)
# print(joint_fuits)


# Разделение строки на строки
multiply_text = '''Line1
Line2
Line3'''
lines = multiply_text.splitlines()
# print(lines)

# Удаление пробелов и символов

text = "         Hello World         \n"

# print(text.strip()) # Убираем комбинацию (по умолчанию - пробелы) с обеих сторон
# print(text.lstrip()) # Убираем комбинацию только слева
# print(text.rstrip()) # Убираем комбинацию только справа

text = "***Hello *** World***"
# print(text.strip("*"))
# print(text.replace("*", ""))


# f-строки

name = "John"
age = 22

# 1. f-strings (рекомендуются, начиная с python 3.6)
message = f"Меня зовут {name} и мне {age} лет!"
# print(message)

# 2. format()
message = "Mеня зовут {} и мне {} года".format(name, age)
# print(message)

# 3. %-форматирование (устаревшее)
message = "Меня зовут %s и мне %d лет" % (name, age)
# print(message)

# Форматривание чисел
price = 19.9999
# print(f"Цена: {price:.2f}")
# print(f"Процент: {0.2535:.1%}")
# print(f"Число: {10000000:,}")


# ПОЛЕЗНЫЕ МЕТОДЫ
# Выравнивание текста

text = "Hello"
# print(text.ljust(10))
# print(text.rjust(10))
# print(text.center(10))
# print(text.center(10, "*"))

# Проверки и преобразования
filename = "document.pdf"
# print(filename.startswith('doc'))
# print(filename.endswith('.pdf'))


# Трансляция символов
text = "hello world"
translation = text.maketrans("hello", "HELLO")
print(text.translate(translation))