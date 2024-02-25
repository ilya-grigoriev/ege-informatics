file = open('../../data/26-files/26-k3.txt', encoding='utf-8')

_, k, m = map(int, file.readline().split())

scores = map(int, file.readlines())
sorted_scores = sorted(scores, reverse=True)

wins = sorted_scores[:k]
sorted_scores = sorted_scores[k:]
pre_wins = sorted_scores[:m]

file.close()

print(min(wins), min(pre_wins))
