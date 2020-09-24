from random import *
import numpy as np
import turtle


number_of_turtles = 25
steps_of_time_number = 100
ay_0 = 1
dt = 0.1
ax_0 = 1
pool = [(turtle.Turtle(shape='circle'), randint(1, 20), 
        randint(-100, 100), randint(1, 20), randint(-100, 100), 
        randint(-180, 180)) for i in range(number_of_turtles)]
    
for turtley, vy_0, y_0, vx_0, x_0, angle in pool:
    turtley.penup()
    turtley.shapesize(0.5, 0.5, 1)
    turtley.speed(np.sqrt(vy_0**2+vx_0**2))
    turtley.goto(x_0, y_0)
    turtley.right(angle) 
    
for i in range(steps_of_time_number): 
    for turtley, vy_0, y_0, vx_0, x_0, angle in pool:
        y_1 = y_0 + dt*vy_0
        vy_1 = vy_0 + dt*ay_0
        x_1 = x_0 + dt*vx_0
        vx_1 = vx_0 + dt*ax_0
        if y_1<-100:
            y_1 += 200
        if y_1>100:
            y_1 -= 200
        if x_1<-100:
            x_1 += 200
        if x_1>100:
            x_1 -= 200 
        y_0 = y_1
        x_0 = x_1
        vy_0 = vy_1
        vx_0 = vx_1
        turtley.goto(x_1, y_1)
        turtley.forward(np.sqrt((vy_0**2 + vx_0**2)*dt**2))
      
        