# Неприжившиеся саженцы - это те места, где ничего не растет.
# Исходя из условий задачи, нам подходят именно те места, где есть k пустых мест.

file = open('data/26-files/26-79.txt', encoding='utf-8')
n, k = map(int, file.readline().split())

lines = [map(int, line.split()) for line in file.readlines()]

rows = dict()
for line in lines:
    row, n = line
    if row not in rows:
        rows[row] = []
    rows[row].append(n)
    rows[row].sort()

for row, trees in rows.items():
    for left, right in zip(trees, trees[1:]):
        if (right - left - 1) == k:   # Делаем -1, т.к. ,например, между 30 и 34 деревом 3 саженца, а не 4.
            # Нам нужен максимальный ряд, так что смысла в дополнительных условиях проверки нет.
            max_row = row
            min_n = left + 1  # Прибавляем к левому дереву 1, т.к. нам нужен минимальный номер неприжившегося
            # саженца (а он будет слева от left дерева).

print(max_row, min_n)

file.close()
