file = open('../../data/26-files/26-71.txt', encoding='utf-8')
n, s = map(int, file.readline().split())

items = [map(int, item.split()) for item in file.readlines()]
dct = dict()
for code, item in items:
    if code not in dct:
        dct[code] = []
    dct[code].append(item)
    dct[code].sort()

exc_items = 0   # Общее кол-во оставшихся товаров кодов после алгоритма
max_exc_items = float('-inf')   # Максимальное число оставшихся элементов
code_with_max_exc_items = float('-inf')   # Код, где находится это максимальное число ост. элементов
for code, items in dct.items():
    k = 0
    while items:
        if k + items[0] <= s:
            k += items[0]
            del items[0]   # Удаляем минимальный элемент, пока не превышаем допустимый вес
        else:
            exc_items += len(items)  # добавляем кол-во оставшихся для данного кода товаров
            if len(items) > max_exc_items:  # если это кол-во оставшихся больше текущего максимального, то ...
                max_exc_items = len(items)  # обновляем "рекорд"
                code_with_max_exc_items = code  # записываем код "рекорда"
            break

print(exc_items, code_with_max_exc_items)
file.close()
