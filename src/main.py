import colorgram
from turtle import Turtle, Screen
import turtle as t
import random
# # we are going to get the 6 color from our image
# colors = colorgram.extract('F:\python practice\hirst_painting\demoreader\src\hirst.jpg',10)

# # we have created a empty list which is used for storing the tuple color
# color_list = []

# # now i am going to find the size of the color we have extracted from the image
# size = len(colors)

# for i in range(0,size):
#     first_color = colors[i]
#     rgb = first_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     tuple_color = (r,g,b)
#     color_list.append(tuple_color)
coloer_picker = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), 
(125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85)] 
# print(coloer_picker)


# creating the object of the Turtle model
temp = Turtle()
screen = Screen()


# i need to speed up the turtle
temp.speed("fastest")


# # seting up the position in x and y cordinate
# temp.penup()
# temp.setpos(-200,-100)
# t.colormode(255)


def draw(y):
    # seting up the position in x and y cordinate
    temp.penup()
    temp.hideturtle()
    temp.setpos(-200,-y)
    t.colormode(255)
    for i in range(len(coloer_picker)):
        # print(temp.color(coloer_picker[6]))
        temp.color(coloer_picker[random.randint(i, len(coloer_picker)-1)])
        # designing the dot..
        temp.dot(20)
        temp.penup()
        temp.forward(50)

for i in range(100):
    if i%2==0:
        temp.penup()
    else:
        draw(i*20)
    # temp.penup()
    # temp.setpos(-200,-100)
    # temp.right(90)
    # temp.forward(50)
    # temp.right(90)
    # temp.pendown()
    # draw()


# temp.forward(100)
# defining a method that will do when the user click the screen it will close..
screen.exitonclick()

