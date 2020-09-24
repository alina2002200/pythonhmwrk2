import turtle
import numpy as np
turtle.shape('turtle')

def strmm(x, y, Vx, Vy):
    ay = -9.8
    dt = 0.01
    for i in range(1000):
       
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
       
        turtle.goto(x, y)

strmm(0, 0, 10, 15)        