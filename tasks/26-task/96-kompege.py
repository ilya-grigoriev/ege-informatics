# Идея в том, чтобы отсортировать список весов по убыванию и добавлять размер, пока позволяет ограничение.
file = open('data/26-files/26_936.txt')
n, s = map(int, file.readline().split())
sizes = [int(line) for line in file]
sizes.sort(reverse=True)

ways = []   # список из рейсов
while sizes:
    sizes_of_way = []   # список весов для будущего рейса

    for i in range(len(sizes)):
        if (sum(sizes_of_way) + sizes[i]) <= s:
            sizes_of_way.append(sizes[i])
            sizes[i] = 0   # заменяем добавленный вес нулем

    if sizes_of_way:   # если список с весами не пуст
        ways.append(sizes_of_way)

    sizes = [size for size in sizes if size != 0]   # все добавленные веса удаляем из списка

print(len(ways), sum(ways[-1]))

file.close()
