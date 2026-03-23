import turtle
import random
import colorgram
tim = turtle.Turtle()
screen = turtle.Screen()
rgb_colors=[]
color_list=[]
colors = colorgram.extract('image.jpg',30)# Need to be in same directory
print(colors)
for color in colors:
    rgb_colors.append(color.rgb)
for rgb in rgb_colors:
    color_list.append((rgb[0],rgb[1],rgb[2]))
print(color_list)

screen.colormode(255)# This fixed bad color sequence issue

# Incase of image.jpg not availble, uncomment below and delete above code which finally results in the bwlow list
#color_list=[(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157), (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152), (164, 80, 52), (200, 84, 111), (208, 225, 215), (143, 31, 40), (54, 167, 135), (232, 198, 110), (201, 219, 227), (229, 206, 214), (6, 109, 90), (41, 160, 185), (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199), (235, 169, 158), (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217), (69, 39, 50)]
tim.penup()
tim.setpos(-300,-300)
print(tim.position())
print(tim.ycor())
for rows in range(10):
    for columns in range(10):
        tim.dot(20,random.choice(color_list))
        tim.up()
        tim.forward(50)
        tim.down()
    tim.teleport(-300,tim.ycor()+50)


screen.exitonclick()
