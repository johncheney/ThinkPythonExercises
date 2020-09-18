
#Golden Spiral

import turtle
import math
bob = turtle.Turtle()
#print(bob)
"""for i in range(4):
    bob.fd(100)
    bob.lt(90)


turtle.mainloop()"""

t = turtle.Turtle()
t.speed(15)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    


#polygon(bob, 50 , 3) #t also works as a call

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    

def circle(t, r):
    arc(t, r, 360)

def fib(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

  
def fibonacci(n):
    if n == 0
        return 0
    elif n == 1
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2)
        

#code plan: make a list of fib numbers 
# use those as a multiplying factor in drawing the 90 angles by 
# focusing on them as a radial multiplyer 
# see the How to draw spirals using python in the readme file of this code for some help


#Draw the Fibonacci Spiral using Turtle Graphics



fibo_nr = [1,1,2,3, 5, 8, 13, 21, 34,55]  

def draw_square(side_length):  #Function for drawing a square
    for i in range(4):
        forward(side_length)
        right(90)

nr_squares=len(fibo_nr)

factor = 3                        #Enlargement factor
penup()
goto(50,50)                  #Move starting point right and up
pendown()
for i in range(nr_squares):
    draw_square(factor*fibo_nr[i]) #Draw square
    penup()                        #Move to new corner as starting point
    forward(factor*fibo_nr[i])
    right(90)
    forward(factor*fibo_nr[i])
    pendown()
        
penup()
goto(50,50)       #Move to starting point
setheading(0)   #Face the turtle to the right
pencolor('red')
pensize(3)
pendown()
#Draw quartercircles with fibonacci numbers as radius
for i in range(nr_squares):
    circle(-factor*fibo_nr[i],90)  # minus sign to draw clockwise

