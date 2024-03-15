# Идея заключается в том, чтобы подсчитывать кол-во входов и выходов для каждого момента времени. Данные записываются в словарь.
# Например, если кто-то зашел в 10 (чего-то), а другой вышел в это время, то сначала делаем +1, а затем -1.
# В итоге, получаем, что в этот момент времени было как бы ноль посещений.

# Стоит учесть эти моменты в конце, когда будет подсчет пиков посещений.
# Например, для времени 10 (чего-то) ноль посещений, т.к. кто-то вышел и кто-то вошел.
# Если мы добавим в список пиков посещений то же число, что было до времени 10 (чего-то), то это
# будет ошибкой, т.к. никаких посещений в момент 10 (чего-то), можно сказать, не было.

file = open('data/26-files/26_9847.txt')
file.readline()
lines = [map(int, line.split()) for line in file]

traffic = dict()

for line in lines:
    start, end = line

    traffic[start] = 1 if start not in traffic else traffic[start] + 1
    traffic[end] = -1 if end not in traffic else traffic[end] - 1

peaks = [0]
for enter_or_exit in sorted(traffic.keys()):
    if traffic[enter_or_exit]:
        peaks.append(peaks[-1] + traffic[enter_or_exit])

max_peak = max(peaks)
print(peaks.count(max_peak), max_peak)

file.close()
