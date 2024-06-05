from turtle import *

tracer(0) # черепашка рисует моментально

K = 10
# перенавправления (right, left) не надо увеличивать, т.к. это всего лишь поворот на месте, а не движение.

# делаем разметку
penup()
for x in range(-20, 50):
    for y in range(-20, 50):
        goto(x * K, y * K)
        dot()

home() # возвращаем черепашку в самый центр (начало)
left(90) # повернуть черепашку, чтобы смотрела вверх (по умолчанию смотрим вправо)

pendown()

for _ in range(2):
    forward(23 * K)
    left(90)
    back(27 * K)
    left(90)

penup()

back(5 * K)
right(90)
forward(11 * K)
left(90)

pendown()

for _ in range(2):
    forward(26 * K)
    right(90)
    forward(32 * K)
    right(90)

update() # обновляем для tracer()
done() # чтобы экран не пропал
