file = open('data/26-files/26-71.txt', encoding='utf-8')
n, s = map(int, file.readline().split())

items = [map(int, item.split()) for item in file.readlines()]
dct = dict()
for code, item in items:
    if code not in dct:
        dct[code] = []
    dct[code].append(item)
    dct[code].sort()

exc_items = 0   # Кол-во оставшихся товаров для каждого кода после алгоритма
max_exc_items = float('-inf')   # Максимальное число оставшихся элементов
code_with_max_exc_items = float('-inf')   # Код, где находится это максимальное число ост. элементов
for code, items in dct.items():
    k = 0
    while items:
        if k + items[0] <= s:
            k += items[0]
            del items[0]   # Удаляем минимальный элемент, пока не превышаем допустимый вес
        else:
            exc_items += len(items)
            if len(items) > max_exc_items:
                max_exc_items = len(items)
                code_with_max_exc_items = code
            break

print(exc_items, code_with_max_exc_items)
file.close()
