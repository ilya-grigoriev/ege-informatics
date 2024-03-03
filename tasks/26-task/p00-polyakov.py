# Идея заключается в том, чтобы заменить последний вес, которые добавим при обычной сортировке,
# на больший. Этот "больший вес" можно обнаружить просто пройдясь по убыванию размеров.
file = open('data/26-files/26.txt')

s, n = map(int, file.readline().split())
sizes = [int(line) for line in file]
sizes.sort()

valid_sizes = []
for size in sizes:
    if (sum(valid_sizes) + size) <= s:   # проверка на возможность добавления текущего размера в список допустимых
        valid_sizes.append(size)
    else:
        break

available_size = valid_sizes[-1] + (s - sum(valid_sizes))   # доступное место, которое можно заменить большим числом
# Т.к. нужно сохранять максимальное кол-во пользователей, то можно заменить только последнее число.

for size in sizes[::-1]:   # проходимся с конца (т.е. по убыванию)
    if size <= available_size:   # если текущий размер меньше доступного или равен ему, то он подходит
        valid_sizes[-1] = size
        break

print(len(valid_sizes), max(valid_sizes))

file.close()
