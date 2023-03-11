# Импорт модулей
import random
import datetime

# Функция сложения float с учетом, что в минуте 60 секунд
def add_fun(songs_time):
    # Список с минутами и секундами
    total_time = [0, 0]
    for song in songs_time:
        whole_number = int(song[1])  # целая часть числа
        fractional_number = int(song[1] * 100 % 100)  # дробная часть числа в сотых долях
        # Складываем с предыдущим проходом
        total_time[0] += whole_number
        total_time[1] += fractional_number
        # Если сумма секунд превысила 60, добавляем минуту и вычитаем секунды
        if total_time[1] > 60:
            total_time[1] -= 60
            total_time[0]+= 1
    # Возврат результата
    return total_time

# Список списков
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Словарь
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# Выбираем три случайные песни
random_songs = random.sample(my_favorite_songs, 3)
# Выводим результат при помощи функции
print(f"Пункт А: Три песни звучат {add_fun(random_songs)[0]} минут")

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# Выбираем три случайные песни
random_songs_dict = random.sample(list(my_favorite_songs_dict.items()), 3)
# Выводим результат при помощи функции
print(f"Пункт В: Три песни звучат {add_fun(random_songs_dict)[0]} минут")

# Пункт C. Сгенерируйте случайные песни с помощью модуля random

# Создаем список песен из пункта А
songs_list = [song[0] for song in random_songs]
#Генерируем случайные песни
random_songs_list = random.sample(songs_list, k=3, counts=None)
# Создаем список песен из пункта В
songs_list = list(my_favorite_songs_dict.keys())
#Генерируем случайные песни
random_songs_list_dict = random.sample(songs_list, k=3, counts=None)
# Выводим список случайных песен
print(f"Пункт С\А: Случайные песни: {random_songs_list}")
print(f"Пункт С\В: Случайные песни: {random_songs_list_dict}")

# Пункт D. Переведите минуты и секунды в формат времени. Используйте модуль datetime

# Создаем объект datetime используя данные из функции

# Для пункта А
rsa = add_fun(random_songs)
time_list = datetime.time(00, rsa[0], rsa[1]).strftime('%M:%S')
# Для пункта В
rsb = add_fun(random_songs_dict)
time_dict= datetime.time(00, rsb[0],rsb[1]).strftime('%M:%S')
# Выводим результат
print(f"Пункт D\A: Три песни звучат {time_list}")
print(f"Пункт D\B: Три песни звучат {time_dict}")