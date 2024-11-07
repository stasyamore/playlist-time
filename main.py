# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список из кортежа строк и кортежа вещественных чисел
#   * многострочная строка
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_d = [
	("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
	(5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

import random
from datetime import timedelta
from typing import Iterable, Any

def parse_playlist(playlist: str) -> list:
    songs = []
    for line in playlist.strip().split(''):
        parts = line.rsplit('', 1)
        if len(parts) == 2:
            title = parts[0]
            duration = float(parts[1])
            songs.append((title, duration))
    return songs



 def get_duration(playlist: Iterable, n: int) -> timedelta:
    """Возвращает общее время звучания n случайных песен из плейлиста."""