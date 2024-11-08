from turtle import *
import numpy,random
angle = float(input("angle  "))
penSize = float(input("width  "))
turt = Turtle()
turt.width(penSize)
speed = 10
turt.speed = speed
colormode(255)
try:
    for k in range(100):
        if(k == 0):
            k = 1
        for i in numpy.arange(0.0001 * k):
            turt.forward(speed * k)
        turt.left(angle)
        turt.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
except:
    pass