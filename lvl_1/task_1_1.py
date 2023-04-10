# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение:

# Преобразуем строку в список, разбивая по запятой
song_list = my_favorite_songs.split(', ')
# Выводим первую песню
print(song_list[0])
# Выводим последнюю песню
print(song_list[-1])
# Выводим вторую песню
print(song_list[1])
# Выводим предпоследнюю песню
print(song_list[-2])

# Отлично!
