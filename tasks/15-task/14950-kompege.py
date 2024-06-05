import math


def nod(n, m, k):
    return math.gcd(n, m) == k


k = 0
for A in range(1, 1000 + 1):
    results = (
        nod(A, 420, 2) or (not nod(A, x, 12) <= (not nod(110, x, 11)))
        for x in range(1, 1000)
    )
    if all(results):
        k += 1

print(k)
