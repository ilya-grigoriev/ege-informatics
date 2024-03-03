# Задачка похожа на tasks/26-task/p00-polyakov.py, только тут, нужно будет изменять не только
# последнее число, но и предпоследнее и т.д.
file = open('data/26-files/26-39.txt')
n, m = map(int, file.readline().split())
weights = [int(line) for line in file]
weights.sort()

_180_to_200 = [weight for weight in weights if 180 <= weight <= 200]
under_180 = [weight for weight in weights if weight < 180]

available_weight = m - sum(_180_to_200)

extra_weights = []   # веса от 0 до 180 невключительно
for weight in under_180:
    if (sum(extra_weights) + weight) <= available_weight:
        extra_weights.append(weight)
    else:
        break

weight_for_replace = available_weight - sum(extra_weights[:-1])   # находим свободное место, исключая последний элемент.
result = []   # список, в котором будут находиться валидные веса меньше 180

while weight_for_replace:   # пока есть свободное место, которое можно заменить
    if weight_for_replace in weights:   # если этот свободный вес есть в списке весов, ...
        extra_weights[-1] = weight_for_replace   # заменяем последний элемент на найденный (который больше)
        result.extend(extra_weights)
        break

    for weight in _180_to_200[::-1]:   # если предыдущее условие не сработало, нужно самим искать вес,
                                       # который меньше свободного места
        if weight < weight_for_replace:
            result.append(weight)   # добавляем найденный вес в список валидных размеров
            del extra_weights[-1]   # удаляем из списка весов от 0 до 180, чтобы он не мешал находить другие веса,
                                    # которыми можно заменить текущие (т.е. проделываем ту же работу)
            break

    if (available_weight - sum(extra_weights) - sum(result)) == 0:   # если после изменения веса свободного места нет,
                                                                     # то мы нашли все возможные валидные веса
        result.extend(extra_weights)   # добавляем оставшиеся веса в список валидных размеров

print(len(result) + len(_180_to_200), sum(result) + sum(_180_to_200))

file.close()
