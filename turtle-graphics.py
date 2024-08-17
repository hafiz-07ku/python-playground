from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red", "green")

# draw triangle, square, pentagon, hxagon, heptagon, octagon, nonagon, decagon using turtle
initialMoves = 100
shapeMoves = initialMoves
turtle.forward(initialMoves)
for i in range(3, 11):
    for j in range(i):
        turtle.left(360 / i)
        turtle.forward(initialMoves)


myScreen = Screen()
myScreen.exitonclick()