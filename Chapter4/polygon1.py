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



def flower(t, r, angle, n):
    for i in range(n):
        arc(t, r, angle)
        t.lt(90)
        arc(t, r, angle)
        n1 = (360 / n)
        t.lt(n1 )
        turtle.mainloop()


def pie(t, length, n):
    for i in range(n):
        a1 = (360 / n)
        print(a1)
        a2 = (180 - ((180 - a1)/2))
        opp = ( math.sqrt(2*(length**2) - ((2*length * length)) * (math.cos(math.radians(a1)))))
        #print(opp)
        t.fd(length)
        t.lt(a2)
        t.fd(opp)
        t.lt(a2)
        t.fd(length)
        t.lt(180)

    
        
       

#flower(t, 100, 90, 18)

#for i in range(26,0,-1):
    #pie(t, 200, i)
    #t.clear()

#for i in range(4):
    #pie(t, 200, 5)
