from random import *
import turtle
import numpy as np


turtle.shape('turtle')
turtle.speed(0)


for i in range(100):
    turtle.forward(randint(0, 30))
    turtle.right(randint(0, 360))
