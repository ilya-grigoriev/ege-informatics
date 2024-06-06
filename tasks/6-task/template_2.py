# Чертежник
from turtle import *

tracer(0)
k = 25
screensize(2000, 2000)

pendown()
for _ in range(7):
    goto(
        xcor() + 6 * k,
        ycor() + (-9 * k),
    )   # смещаемся на какие-то координаты, считая от текущих
    # Текущие координаты - это xcor() и ycor().
    goto(xcor() + (-6 * k), ycor() + 2 * k)
    goto(xcor() + 12 * k, ycor() + 3 * k)

penup()

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot()

update()
done()
