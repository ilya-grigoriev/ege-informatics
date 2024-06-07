file = open('../../data/26-files/26-70.txt', encoding='utf-8')
file.readline()
items = sorted([int(i) for i in file.readlines()])

new_items = []   # Список слитков, которые необходимо добавить
sum_items = [items[0]]   # Список слитков для суммирования меньших слитков

for item in items[1:]:
    if (item - sum(sum_items)) < 1:  # Проверяем, что разницы меньше единицы
        sum_items.append(item)
    else:
        new_item = (item - sum(sum_items)) - 1   # Находим необходимую массу слитка, который надо заказать. Вычитание единицы делаем, т.к. разница слитка и суммарного веса меньших слитков должна быть не более чем на 1.

        new_items.append(new_item)
        sum_items.append(item)

print(len(new_items), sum(new_items))

file.close()
