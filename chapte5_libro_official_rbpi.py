import turtle
import random

pat=turtle.Turtle()

#pat.forward(100)

turtle.Screen().bgcolor("red")
#pat.color("cyan")

colores=["cyan","purple","white","blue"]

for i in range(2):
    pat.forward(100)
    pat.right(60)
    pat.forward(100)
    pat.right(120)

for i in range(10):
    pat.right(36)

for i in range(10):
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.color(random.choice(colores))
    pat.right(36)


