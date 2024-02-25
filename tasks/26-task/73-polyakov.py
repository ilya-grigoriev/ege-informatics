file = open('data/26-files/26-73.txt', encoding='utf-8')
file.readline()

elements = [map(int, element.split()) for element in file.readlines()]
dct = dict()   # Словарь, где ключом является номер строки, а значением - список из столбцом (элементов)
for row, col in elements:
    if row not in dct:
        dct[row] = []
    dct[row].append(col)
    dct[row].sort()

max_length = float('-inf')
max_row = float('-inf')
for row, cols in dct.items():
    ind = 0
    length = 1   # Минимальная длина каждой цепочки
    cols = list(set(cols))   # Избавляемся от дубликатов
    while ind != (len(cols) - 1):
        if cols[ind + 1] - cols[ind] == 1:   # Проверяем, что следующий элемент стоит рядом
            length += 1
        else:   # Иначе получается, что следующий элемент не является рядом стоящим
            if length > max_length:
                max_length = length
                max_row = row
            length = 1
        ind += 1

print(max_length, max_row)
file.close()
