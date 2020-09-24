from random import *
import turtle
import numpy as np
turtle.shape('turtle')

inp = open('ch3.txt', 'r')

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


Zero = eval(inp.readline().rstrip())
One = eval(inp.readline().rstrip())
Two = eval(inp.readline().rstrip())
Three = eval(inp.readline().rstrip())
Four = eval(inp.readline().rstrip())
Five = eval(inp.readline().rstrip())
Six = eval(inp.readline().rstrip())
Seven = eval(inp.readline().rstrip())
Eight = eval(inp.readline().rstrip())
Nine = eval(inp.readline().rstrip())
Next = eval(inp.readline().rstrip())

All(One, Next)
All(Four, Next)
All(One, Next)
All(Seven, Next)
All(Zero, Next)
All(Zero, Next)

