# ПРАВИЛЬНО
# def my_function():
#     if condition:
#         print("Hello")
#         another_function()

# НЕ ПРАВИЛЬНО

# def   my_function1( ):
#   if condition:
#   print( "Hello")
#             another_function( )

# МАКСИМАЛЬНАЯ ДЛИННА СТРОКИ - 79 символам

# # НЕ ПРАВИЛЬНО
# result = very_long_variable_name1 + very_long_variable_name2 - very_long_variable_name3 * very_long_variable_name4 // very_long_variable_name5
#
# # ПРАВИЛЬНО
# result = (very_long_variable_name1 +
#           very_long_variable_name2 -
#           very_long_variable_name3 *
#           very_long_variable_name4 //
#           very_long_variable_name5)


# # НЕ ПРАВИЛЬНО
# x=5
# y=10
# result=(x+y)*(x-y)
#
# # ПРАВИЛЬНО
# x = 5
# y = 10
# result = (x + y) * (x - y)

# # ПРАВИЛЬНО
# # переменные и функции - snake_case
# user_name = 'Jhon'
# calculate_total_price()
#
# # классы - PascalCase
# class UserProfile:
#     pass
#
# # константы - UPPER_CASE
# MAX_USERS = 100
# API_KEY = 'secret'
#
# # НЕ ПРАВИЛЬНО
# UserName = 'Jhon'
# calculateRoralPrice()
# max_users = 100

# # НЕ ПРАВИЛЬНО
# my_list = [1,2,3 , 4,5]
# my_function(arg1,arg2 , arg3)
#
# # ПРАВИЛЬНО
# my_list = [1, 2, 3, 4, 5]
# my_function(arg1, arg2, arg3)


# # НЕ ПРАВИЛЬНО
# import random
# import sys
# class MyClass:
#     def __init__(self, n):
#         self.n = n
#     def method_1(self):
#         pass
#     def method_2(self):
#         pass
# def standalone_fun():
#     pass
#
#
# # ПРАВИЛЬНО
# import random
# import sys
#
#
# class MyClass1:
#     def __init__(self, n):
#         self.n = n
#
#     def method_1(self):
#         pass
#
#     def method_2(self):
#         pass
#
#     def method_3(self):
#         pass
#
#
# def standalone_fun2():
#     pass


# # НЕ ПРАВИЛЬНО
#
# #Это комментарий без пробела
# x = 5#Комментарий
#
# # ПРАВИЛЬНО
# # Это комментарий с пробелом
# x = 5 # Комментарий
#
# '''
# Это многострочный комментарий
# Он чистый и опрятный
# Все спасибо, кто смотрит это долгое видео!
# '''


# # НАРУШЕНИЕ
# class userData:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def display_info(self):
#         print(f"Name:{self.Name}, Age:{self.Age}")
#
# def Calculate_Sum(a,b):
#     result=a+b
#     return result
#
# # ИСПРАВЛЕНО
# class UserData:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def display_info(self):
#         print(f"Name: {self.Name}, Age: {self.Age}")
#
# def calculate_sum(a, b):
#     result = a + b
#     return result



































