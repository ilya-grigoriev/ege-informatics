from itertools import chain


def find_couples(start_n, nums):
    """Поиск пар с разностью >= 3

    Parameters
    ----------
    start_n : int
        Начальное число.
    nums : Iterable[int]
        Список из чисел, с которыми будет сравниваться текущее число.

    """
    couples = []  # Пары (число, число с разницей >= 3)
    cur = n   # Ставим начальное число как текущее
    ind = 0
    while ind != (
        len(nums) - 1
    ):   # Заканчиваем итерацию, как только доходим до последнего элемента (по индексации)
        if nums[ind] - cur >= 3:   # Сравниваем разность двух чисел
            couples.append((cur, nums[ind]))   # Добавляем эту пару чисел
            cur = nums[ind]   # Текущим числом становится число с разницей >= 3
        ind += 1   # На каждой итерации прибавляем к индексации 1.
    return couples


file = open('../../data/26-files/26-89.txt', encoding='utf-8')

nums = sorted([int(n) for n in file.readlines()[1:]])

vars = []
min_first = float('-inf')
max_len = float('-inf')
for ind, n in enumerate(nums, start=1):
    if ind == len(nums):
        break

    couples = find_couples(
        n,
        nums[ind:],
    )   # Передаем в качестве аргументов текущее число и список с индексом этого числа + 1, чтобы его не учитывать.
    couples = chain(
        *couples,
    )   # С помощью itertools.chain соединяем все пары в один массив чисел
    couples = tuple(set(couples))   # Убираем повторяющиеся числа

    if couples:
        if len(couples) > max_len:
            if couples[0] > min_first:
                min_first = couples[0]
            max_len = len(couples)

file.close()
print(min_first, max_len)
