file = open('data/26-files/26-89.txt', encoding='utf-8')

file.readline()
nums = sorted([int(n) for n in file.readlines()], reverse=True)

max_n = nums[0]   # Максимальным числом будет первое, т.к. массив уже отсортирован
couples = [max_n]   # Создаем список, в котором будут хранится числа с разницей между собой >= 3
for i in range(1, len(nums)):
    if (couples[-1] - nums[i]) >= 3:   # Сравниваем последнее число из массива чисел с разницей >= 3 и текущее число по индексации
        couples.append(nums[i])

print(len(couples), min(couples))

file.close()

# Проблемы вариации для последней коробки не будет, т.к. мы уже отсортировали все коробки.
# Значит, последняя добавленная в `couples` коробка будет максимально возможной среди всех последних коробок для `couples`.
