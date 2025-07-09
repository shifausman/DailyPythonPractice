#square
from turtle import Turtle
t=Turtle()
n=1
while(n!=5):
    t.forward(100)
    t.right(90)
    n+=1"""

#random walk
"""from turtle import Turtle
import random
def randomWalk(t, turns, distance = 20):
    for x in range(turns):
        t.left(random.randint(0, 360))
        t.forward(distance)
randomWalk(Turtle(), 40)"""

#yellow hexagon
"""import turtle
t=turtle.Turtle()

s=turtle.Screen()
s.bgcolor("black")

t.color("white","yellow")
t.pensize(5)

t.begin_fill()
for _ in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()

t.hideturtle()
t.turtledone()"""

#folwer
"""import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
flower = turtle.Turtle()
flower.speed(10)
flower.color("red")

# Function to draw a petal
def draw_petal():
    flower.begin_fill()
    flower.circle(100, 60)      # Draw arc
    flower.left(120)
    flower.circle(100, 60)      # Draw arc again
    flower.left(120)
    flower.end_fill()

# Draw flower with 6 petals
for _ in range(6):
    draw_petal()
    flower.right(60)

# Draw the center of the flower
flower.color("yellow")
flower.goto(0,-20)
flower.begin_fill()
flower.circle(20)
flower.end_fill()

# Hide turtle and finish
flower.hideturtle()
turtle.done()

#chessboard
import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
chess = turtle.Turtle()
chess.speed(5)
chess.penup()

# Size of each square
square_size = 50

# Draw the chessboard
def draw_chessboard():
    start_x = -200
    start_y = 200

    colors = ["white", "black"]

    for row in range(8):
        for col in range(8):
            x = start_x + col * square_size
            y = start_y - row * square_size
            chess.goto(x, y)
            chess.fillcolor(colors[(row + col) % 2])
            chess.begin_fill()
            for _ in range(4):
                chess.pendown()
                chess.forward(square_size)
                chess.right(90)
            chess.end_fill()
            chess.penup()

# Draw the board
draw_chessboard()

# Hide turtle and finish
chess.hideturtle()
turtle.done()

#STAR
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
star = turtle.Turtle()
star.color("yellow")
star.pensize(2)
star.speed(2)
star.color("yellow")


# Draw a star
for i in range(5):
    star.forward(100)
    star.right(144)

# Hide turtle and display result
star.hideturtle()
turtle.done()



