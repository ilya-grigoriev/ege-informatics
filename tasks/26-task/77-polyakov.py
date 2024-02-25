file = open('data/26-files/26-77.txt', encoding='utf-8')
file.readline()

items = [map(int, item.split()) for item in file.readlines()]

dct = dict()
for page, n in items:
    if page not in dct:
        dct[page] = []
    dct[page].append(n)
    dct[page].sort()

empty_places = 0   # Общее кол-во свободных мест
max_empty_places = float('-inf')   # Максимальное кол-во свободных мест на какой-то странице
page_with_max_empty_places = float('-inf')   # Страница с макс. кол-вом свободных мест
for page, stickers in dct.items():
    stickers = set(stickers)   # Избавляемся от повторений

    empty_places_cur = 8 - len(stickers)   # Узнаем кол-во свободных мест
    empty_places += empty_places_cur

    if empty_places_cur >= max_empty_places:
        max_empty_places = empty_places_cur
        page_with_max_empty_places = page

print(empty_places, page_with_max_empty_places)

file.close()
