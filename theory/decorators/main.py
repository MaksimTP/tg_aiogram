#   Декораторы — это обёртки вокруг Python-функций (или классов), которые изменяют работу того, к чему они применяются. Декоратор максимально абстрагирует собственные механизмы. А синтаксические конструкции, используемые при применении декораторов, устроены так, чтобы они как можно меньше влияли бы на код декорируемых сущностей. Разработчики могут создавать код для решения своих специфических задач так, как привыкли, а декораторы могут использовать исключительно для расширения функционала своих разработок. Всё это — очень общие утверждения, поэтому перейдём к примерам.

# В Python декораторы используются, в основном, для декорирования функций (или, соответственно, методов). Возможно, одним из самых распространённых декораторов является декоратор @property:



# class Rectangle: # Объявление класса
#     def __init__(self,a,b): # Объявление конструктора
#         self.a = a # a и b - атрибуты объектов класса
#         self.b = b

#     @property # это декоратор - здесь он позволяет обращаться к функции area, как к атрибуту.
#     def area(self): # Метод/Функция класса
#         return self.a * self.b # Возвращаемое значение - площадь
    
# rect = Rectangle(5, 6) # Создание экземпляра класса
# print(rect.area) # Вызываем функцию area как атрибут класса

# print(rect.area()) - выйдет ошибка, т.к. rect.area - это уже число, а rect.area() будет похоже на 30()



# ----------Как работают декораторы?--------

# Размещение конструкции @property перед определением функции равносильно использованию конструкции вида area = property(area). Другими словами, property — это функция, которая принимает другую функцию в качестве аргумента и возвращает ещё одну функцию. Именно этим и занимаются декораторы.


# ----------Декораторы функций-----------

#      ------Декоратор retry-------




# import time

# def retry(func):
#     def _wrapper():
#         try:
#             print(f'Находимся в блоке try. Пробуем исполнить функцию {func.__name__}')
#             time.sleep(3)
#             func()
#         except:
#             print(f'Находимся в блоке except. Пробуем исполнить функцию {func.__name__}')
#             time.sleep(5)
#             func()
#     return _wrapper

# @retry
# def might_fall():
#     print('might_fall')
#     raise Exception

# might_fall()






# def retry(max_retries):
#     def retry_decorator(func):
#         def _wrapper():
#             for _ in range(max_retries):
#                 try:
#                     print('try')
#                     func()
#                 except:
#                     print('except')
#                     time.sleep(3)
#         return _wrapper
#     return retry_decorator

# @retry(2)
# def might_fall():
#     print('might_fall')
#     raise Exception


# might_fall()




# -------------Декоратор timer---------

# Напишем ещё один полезный декоратор — timer («таймер»). Он будет измерять время выполнения декорированной с его помощью функции:




# import functools
# import time
# from typing import Any

# def timer(func):
#     @functools.wraps(func)
#     def _wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         runtime = time.perf_counter() - start
#         print(f'{func.__name__} сработала за {runtime:.6f} секунд')
#         return result
#     return _wrapper


# @timer
# def complex_calculation():
#     '''Сложные вычисления'''
#     time.sleep(1)
#     return 42


# print(complex_calculation())




# Видно, что декоратор timer выполняет какой-то код до и после вызова декорируемой функции. В остальном же он работает точно так же, как декоратор, рассмотренный в предыдущем разделе. Но при его написании мы воспользовались и кое-чем новым.

#  --------Декоратор functools.wraps---------



# Вот что получится без @functools.wraps и с @functools.wraps:





# print(complex_calculation.__module__)
# print(complex_calculation.__name__)
# print(complex_calculation.__qualname__)
# print(complex_calculation.__doc__)
# print(complex_calculation.__annotations__)





#      --------Декораторы классов--------


# import time

# @timer
# class MyClass:
#     def complex_calc(self):
#         time.sleep(1)
#         return 42
    

# my_obj = MyClass()
# my_obj.complex_calc()









# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#         self.counter = 0

#     def __call__(self, *args, **kwargs):
#         self.func(*args, **kwargs)
#         self.counter += 1
#         print(f'Фyнкция вызвана {self.counter} раз')


# @MyDecorator
# def some_func():
#     return 42


# some_func()
# some_func()
# some_func()
# some_func()
# some_func()








# Взгляните на этот код:




# def add_calc(target):

#     def calc(self):
#         return 42
    
#     target.calc = calc
#     return target


# @add_calc
# class MyClass:
#     def __init__(self):
#         print("MyClass __init__")


# my_obj = MyClass()
# print(my_obj.calc())







#          ---------Использование декораторов-------
#   -------Декораторы в стандартной библиотеке Python-----


#            ----------Декоратор property--------





# class MyClass:
#     def __init__(self, x) -> None:
#         self.x = x

#     @property
#     def x_doubled(self):
#         return self.x * 2
    
#     @x_doubled.setter
#     def x_doubled(self, x_doubled):
#         self.x = x_doubled // 2


# my_obj = MyClass(5)
# print(my_obj.x_doubled) # 10
# print(my_obj.x) # 5
# my_obj.x_doubled = 100
# print(my_obj.x_doubled)
# print(my_obj.x)


#           ---------Декоратор staticmethod-------





# class Class:
#     @staticmethod
#     def the_static_method(arg1):
#         return arg1
    
# print(Class.the_static_method(4))






#           ---------Декоратор functools.cache-------

# При работе с функциями, выполняющими сложные вычисления, может понадобиться кешировать результаты их работы.

# Например, можно соорудить нечто вроде такого кода:




# import time

# def something_complex():
#     time.sleep(3)
#     return 321**3


# _cached_result = None

# def complex_calculations():
#     global _cached_result

#     if _cached_result is None:
#         _cached_result = something_complex()
#         print(_cached_result)
#     return _cached_result

# complex_calculations()





# from functools import cache

# @cache
# def complex_calculations():
#     return something_complex()





# from dataclasses import dataclass

# @dataclass
# class InventoryItem:
#     name: str
#     unit_price: float
#     quantity: int = 0

#     def total_cost(self) -> float:
#         return self.unit_price * self.quantity
    

# item = InventoryItem(name = '', unit_price= 12, quantity= 100)
# print(item.total_cost())



# from dataclasses import dataclass
# from dataclasses_json import dataclass_json

# @dataclass_json
# @dataclass
# class InventoryItem:
#     name: str
#     unit_price: float
#     quantity: int = 0

#     def total_cost(self) -> float:
#         return self.unit_price * self.quantity
    

# item = InventoryItem(name = '', unit_price= 12, quantity= 100)
# # print(item.total_cost())

# print(item.to_dict())


