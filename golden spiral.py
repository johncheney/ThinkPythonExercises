
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



