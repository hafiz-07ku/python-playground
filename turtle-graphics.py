from turtle import Turtle, Screen
import random

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red", "green")

# draw triangle, square, pentagon, hxagon, heptagon, octagon, nonagon, decagon using turtle
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "gold", "chartreuse", "blue violet"]
def drawShape(shapesides):
    angle = 360 / shapesides
    for i in range(shapesides):
        turtle.forward(100)
        turtle.left(angle)
for i in range(3, 11):
    turtle.color(random.choice(colors))
    drawShape(i)


myScreen = Screen()
myScreen.exitonclick()