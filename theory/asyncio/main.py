import time




# 2.1

'''
Есть две функции, в каждой есть быстрая и медленная операция. Наша задача - выполнить обе задачи как можно быстрее
'''



# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')


# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')


# def main():
#     fun1(4) # 16
#     fun2(4) # 2.0


# print(time.strftime('%X')) # Замеряем начало запуска программы

# main() # Запуск программы

# print(time.strftime('%X')) # Замеряем конец программы

# Результат - честные 6 секунд.




# # 2.2

# import asyncio # Для asyncio.sleep(x) 
# import time


# async def fun1(x): # префикс async говорит интерпретатору Python, что функция должна выполняться асинхронно
#     print(x**2)
#     await asyncio.sleep(3) # Вместо time.sleep используем asyncio.sleep. Это неблокирующая задержка. Работает так же, но не останавливает интерпретатор в целом.
#     # Также перед вызовом асинхронных функций появился префикс await. Он говорит интерпретатор: "я тут потуплю, ты меня не жди - выполняй другую часть кода, а когда я буду готов, я тебе маякну."
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# async def main():
#     task1 = asyncio.create_task(fun1(4)) # При помощи create_task создали задачи и запустили это все при помощи asyncio.run
#     task2 = asyncio.create_task(fun2(4))

#     await task1
#     await task2


# print(time.strftime('%X'))

# asyncio.run(main())

# print(time.strftime('%X'))

# # Результат - 3 секунды!




# 2.3

# import asyncio
# import time


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# print(time.strftime('%X'))

# loop = asyncio.get_event_loop()
# task1 = loop.create_task(fun1(4))
# task2 = loop.create_task(fun2(4))
# loop.run_until_complete(asyncio.wait([task1, task2]))

# print(time.strftime('%X'))



# # 3.1 Немножко разберемся с типами. Вернемся к примеру 2.1
# import time


# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')


# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')


# def main():
#     fun1(4)
#     fun2(4)


# print(type(fun1)) # <class 'function'>

# print(type(fun1(4))) # <class 'NoneType'>



# # 3.2 
# import asyncio
# import time


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))

#     await task1
#     await task2


# print(type(fun1)) # <class 'NoneType'>

# print(type(fun1(4))) # <class 'coroutine'> - Ничто превратилось в нечто!


# # 4.1

# import asyncio


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))

#     print(type(task1))
#     print(task1.__class__.__bases__)

#     await task1
#     await task2


# asyncio.run(main())




# # 4.2

# from time import sleep
# from asyncio import create_task
# def fun1(x):
#     print(x**2)
    
#     # запустили ожидание
#     sleep(3)
    
#     print('fun1 завершена')


# def fun2(x):
#     print(x**0.5)
    
#     # запустили ожидание
#     sleep(3)
    
#     print('fun2 завершена')


# def main():
#     # создали конкурентную задачу из функции fun1
#     task1 = create_task(fun1(4))
    
#     # создали конкурентную задачу из функции fun2
#     task2 = create_task(fun2(4))

#     # запустили задачу task1 
#     task1
    
#     # запустили task2
#     task2


# main()



# # 4.3


# import asyncio
# import time


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')


# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')


# async def main():
#     await fun1(4)
#     await fun2(4)


# print(time.strftime('%X'))

# asyncio.run(main())

# print(time.strftime('%X'))

# # 5.1

# import asyncio


# # имитация  асинхронного соединения с некой периферией
# async def get_conn(host, port):
#     class Conn:
#         async def put_data(self):
#             print('Отправка данных...')
#             await asyncio.sleep(2)
#             print('Данные отправлены.')

#         async def get_data(self):
#             print('Получение данных...')
#             await asyncio.sleep(2)
#             print('Данные получены.')

#         async def close(self):
#             print('Завершение соединения...')
#             await asyncio.sleep(2)
#             print('Соединение завершено.')

#     print('Устанавливаем соединение...')
#     await asyncio.sleep(2)
#     print('Соединение установлено.')
#     return Conn()


# class Connection:
#     # этот конструктор будет выполнен в заголовке with
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port

#     # этот метод будет неявно выполнен при входе в with
#     async def __aenter__(self):
#         self.conn = await get_conn(self.host, self.port)
#         return self.conn

#     # этот метод будет неявно выполнен при выходе из with
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()


# async def main():
#     async with Connection('localhost', 9001) as conn:
#         send_task = asyncio.create_task(conn.put_data())
#         receive_task = asyncio.create_task(conn.get_data())

#         # операции отправки и получения данных выполняем конкурентно
#         await send_task
#         await receive_task


# asyncio.run(main())


# # 5.2
# import asyncio
# import time
# from aiohttp import ClientSession


# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             print(f'{city}: {weather_json["weather"][0]["main"]}')


# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))

#     for task in tasks:
#         await task


# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

# print(time.strftime('%X'))

# asyncio.run(main(cities))

# print(time.strftime('%X'))


# # 5.3 


# import time
# import requests


# def get_weather(city):
#     url = f'http://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

#     weather_json = requests.get(url=url, params=params).json()
#     print(f'{city}: {weather_json["weather"][0]["main"]}')


# def main(cities_):
#     for city in cities_:
#         get_weather(city)


# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

# print(time.strftime('%X'))

# main(cities)

# print(time.strftime('%X'))




# # 5.4

# import asyncio
# import time
# from aiohttp import ClientSession


# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             return f'{city}: {weather_json["weather"][0]["main"]}'


# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))

#     results = await asyncio.gather(*tasks)

#     for result in results:
#         print(result)


# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

# print(time.strftime('%X'))

# asyncio.run(main(cities))

# print(time.strftime('%X'))