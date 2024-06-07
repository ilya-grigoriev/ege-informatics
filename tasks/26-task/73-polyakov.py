file = open('../../data/26-files/26-73.txt', encoding='utf-8')
file.readline()

elements = [map(int, element.split()) for element in file.readlines()]
dct = (
    dict()
)   # Словарь, где ключом является номер строки, а значением - список, состоящий из чувствительных элементов
for row, col in elements:
    if row not in dct:
        dct[row] = []
    dct[row].append(col)
    dct[row].sort()

max_length = float('-inf')
max_row = float('-inf')
for row, cols in dct.items():
    ind = 0
    cur_length = 1   # Длина текущей цепочки. Минимальная длина каждой цепочки - 1
    cols = list(set(cols))   # Избавляемся от дубликатов

    while ind != (len(cols) - 1):
        if (cols[ind + 1] - cols[ind] == 1):   # Проверяем, что следующий элемент стоит рядом
            cur_length += 1
        else:   # Иначе получается, что следующий элемент не является рядом стоящим
            if cur_length > max_length:
                max_length = cur_length
                max_row = row

            cur_length = 1  # Сбрасываем значение длины цепочки
        ind += 1

print(max_length, max_row)
file.close()
