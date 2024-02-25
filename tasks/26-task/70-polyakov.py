file = open('data/26-files/26-70.txt', encoding='utf-8')
file.readline()
items = sorted([int(i) for i in file.readlines()])

new_items = []   # Список слитков, которые необходимо добавить
ind = 1   # Индексация для
sum_items = [items[0]]   # Список слитков для суммирования

while ind != len(items):
    if (items[ind] - sum(sum_items)) < 1:
        sum_items.append(items[ind])
    else:
        new_item = (items[ind] - sum(sum_items)) - 1   # Находим необходимую массу слитка

        new_items.append(new_item)
        sum_items.append(items[ind])
    ind += 1

print(len(new_items), sum(new_items))

file.close()
