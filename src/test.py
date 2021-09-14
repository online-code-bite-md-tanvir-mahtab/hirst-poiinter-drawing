# defining the model of the turtle class
from turtle import Turtle, Screen
import random 
import turtle as t


# creating the object of the turtle model class
tummy = Turtle()
screen = Screen()


coloer_picker = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), 
(125, 36, 24), (223, 224, 228), (167, 106, 56),
 (186, 159, 52), (6, 57, 83), (108, 68, 85)] 

# for speeding up the turtle we are going to do this 
tummy.speed('fastest')
tummy.penup()
tummy.setheading(220)
tummy.forward(290)
tummy.seth(0)

# lets change the mode of the turtle
t.colormode(255)

# now i am going to hide the turtle cursor
tummy.hideturtle()

# we are going to draw the dots 
for dot_count in range(1,101):
    tummy.dot(20,random.choice(coloer_picker))
    tummy.forward(50)
    if dot_count % 10 == 0:
        tummy.setheading(90)
        tummy.forward(50)
        tummy.setheading(180)
        tummy.forward(500)
        tummy.seth(0)
# now when a user tuch the screen the screen will closed
screen.exitonclick()
