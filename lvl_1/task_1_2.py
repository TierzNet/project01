# Импорт модулей
import random
import datetime

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
# Вычисляем общее время звучания трех случайных песен
total_time = sum([song[1] for song in random_songs])
# Выводим результат
print(f"Пункт А: Три песни звучат {total_time:.0f} минут")

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# Выбираем три случайные песни
random_songs_dict = random.sample(list(my_favorite_songs_dict.items()), 3)
# Вычисляем общее время звучания трех случайных песен
total_time_dict = sum([song[1] for song in random_songs_dict])
# Выводим результат
print(f"Пункт В: Три песни звучат {total_time_dict:.0f} минут")

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

# Создаем объект timedelta с количеством секунд, равным общему времени звучания трех случайных песен

# Для пункта А
total_time_td = datetime.timedelta(seconds=total_time * 60)
# Для пункта В
total_time_tdd = datetime.timedelta(seconds=total_time_dict * 60)
# Выводим результат
print(f"Пункт D\A: Три песни звучат {str(total_time_td)[2:-7]}")
print(f"Пункт D\B: Три песни звучат {str(total_time_tdd)[2:-7]}")