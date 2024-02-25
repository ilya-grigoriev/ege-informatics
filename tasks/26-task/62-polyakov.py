file = open('data/26-files/26-62.txt', encoding='utf-8')

n, m = map(int, file.readline().split())
items = [(int(item.split()[0]), item.split()[1]) for item in file.readlines()]
file.close()

dct = dict()
for price, symbol in items:
    if symbol not in dct:
        dct[symbol] = []
    dct[symbol].append(price)
    dct[symbol].sort()

table = [[0 for y in range(len(dct['Q']))] for x in range(len(dct['Z']))]
for x in range(len(table)):
    for y in range(len(table[0])):
        if x != 0 and y != 0:
            table[x][y] = (dct['Z'][x] + dct['Q'][y]) + table[x - 1][y- 1]
        else:
            table[x][y] = (dct['Z'][x] + dct['Q'][y])

valid = []
for x in range(len(table)):
    for y in range(len(table[0])):
        if table[x][y] < price:
            valid.append((x, y))
valid.sort(key=lambda x: (x[0], x[1]))
print(*valid, sep='\n')
