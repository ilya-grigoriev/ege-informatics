# Задачка похожа на tasks/26-task/p00-polyakov.py, только тут, нужно будет изменять не только
# последнее число, но и предпоследнее и т.д.
file = open('../../data/26-files/26-39.txt')
n, m = map(int, file.readline().split())
weights = [int(line) for line in file]
weights.sort()

_180_to_200 = [weight for weight in weights if 180 <= weight <= 200]
under_180 = [weight for weight in weights if weight < 180]

available_weight = m - sum(_180_to_200)

extra_weights = []   # веса от 0 до 180 невключительно, которые можно вместить
for weight in under_180:
    if (sum(extra_weights) + weight) <= available_weight:
        extra_weights.append(weight)
    else:
        break

weight_for_replace = available_weight - sum(extra_weights[:-1])   # находим свободное место, исключая последний элемент.

while weight_for_replace:   # пока есть свободное место, которое можно заменить
    if weight_for_replace in weights:   # если этот свободный вес есть в списке весов, ...
        extra_weights[-1] = weight_for_replace   # заменяем последний элемент на найденный (который больше)
        break # завершаем поиск весов для заполнения

    for weight in under_180:
        if (weight not in extra_weights) and weight_for_replace:
            result.append(weight)
            weight_for_replace -= weight

print(len(extra_weights) + len(_180_to_200), sum(extra_weights) + sum(_180_to_200))

file.close()
