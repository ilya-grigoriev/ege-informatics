# Из примера ясно, что к премиум сегменту относятся последние m телефонов по возрастанию цены.
file = open('data/26-files/26-k5.txt')
n, k, m = map(int, file.readline().split())
phones = [int(line) for line in file]
phones.sort()

budg = phones[:k]   # первые k телефонов по возрастанию цены - самые дешевые -> бюджетные
prem = phones[::-1][:m]   # первые m телефонов по убыванию цены - самые дорогие -> премиум
# Перевернул список для лучшего понимания. Можно было записать phones[-1:-m-1:-1].

print(min(prem), int(sum(budg) / len(budg)))

file.close()
