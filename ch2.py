from random import *
import turtle
import numpy as np
turtle.shape('turtle')


def strmm(A):
    for angle, step in A:
        turtle.right(angle)
        turtle.forward(step)
        
def Nnext(B):
    turtle.penup()
    strmm(B)
    turtle.pendown()
    
    
def All(C, D):
    strmm(C)
    Nnext(D)

k = 20 
m = 2*k
d = k*2**0.5
Zero = [(90, m), (90, k), (90, m), (90, k)]      
One = [(90, m), (180, m), (225, d), (180, d), (45, 0)]
Two = [(90, k), (45, d), (315, k), (180, k), (135, d), (-45, k), (-90, k), (180, k)]
Three = [(90, m), (90, k), (180, k), (-90, k), (-90, k), (180, k), (-90, k), (-90, k), (180, k)]
Four = [(90, m), (180, k), (270, k), (90, k), (180, k), (270, k), (270, k), (90, 0)]
Five = [(180, k), (-90, k), (-90, k), (90, k), (90, k), (180, k), (-90, k), (-90, k), (90, k), (90, k)]
Six = [(180, k), (-90, m), (-90, k), (-90, k), (-90, k), (90, k), (90, k)]
Seven = [(135, d), (315, k), (180, k), (45, d), (225, k), (180, k)]
Eight = [(180, k), (-90, m), (-90, k), (-90, k), (-90, k), (180, k), (-90, k), (90, 0)]
Nine = [(180, k), (-90, k), (-90, k), (90, k), (90, k), (180, k), (-90, m), (90, 0)]
Next = [(0, m)]

All(One, Next)
All(Four, Next)
All(One, Next)
All(Seven, Next)
All(Zero, Next)
All(Zero, Next)
