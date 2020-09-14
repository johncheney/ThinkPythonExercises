import turtle
import math
t = turtle.Turtle()
turtle.width(5)
turtle.speed(5)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)



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
    

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def down(t, length):
    t.lt(270)
    t.fd(length)

def lr(t, length):
    t.fd(length)


def reset(t):
    t1.reset()
    t2.reset()
    t3.reset()
    



# Alphabet in turtle



t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()




def draw_a(t, length):
    t1.lt(255)
    t1.fd(length)
    t2.lt(285)
    t2.fd(length)
    t3.lt(255)
    t3.fd(length*.5)
    t3.lt(105)
    t3.fd(length*.3)
    t1.reset()
    t2.reset()
    t3.reset()


draw_a(t1, 100)

##

def draw_b(t, length):
    t1.lt(270)
    t1.fd(length)
    arc(t2, 25, -90)
    arc(t2, 25, -90)
    t2.lt(180)
    arc(t2, 25, -90)
    arc(t2, 25, -90)
    t1.reset()
    t2.reset()


draw_b(t, 100)

def draw_c(t, length):
    move(t1, 20, 20)
    t1.lt(180)
    arc(t1, 50, -230)
    


draw_c(t, 100)
reset(t)

def draw_d(t, length):
    t1.lt(270)
    t1.fd(length)
    arc(t2, 50, -90)
    arc(t2, 50, -90)
    reset(t)


draw_d(t, 100)

def draw_e(t, length):
    down(t1, length)
    move(t2, 0, 0)
    lr(t2, length*.5)
    move(t2, 0, -50)
    lr(t2, length*.25)
    move(t2, 0, -100)
    lr(t2, length*.5)
    reset(t)


draw_e(t, 100)
    
def draw_f(t, length):
    down(t1, length)
    move(t2, 0, 0)
    lr(t2, length*.5)
    move(t2, 0, -50)
    lr(t2, length*.25)
    reset(t)

draw_f(t, 100)

def draw_g(t, length):
    draw_c(t2, length)
    t1.lt(50)
    move(t1, 10, 50)
    lr(t1, length*.5)
    down(t1, length*.5)
    reset(t)
    

draw_g(t, 100)

def draw_h(t, length):
    down(t1, length)
    move(t1, 0, -50)
    t1.lt(90)
    lr(t1, length*.5)
    move(t1, 50, 0)
    down(t1, length)
    reset(t)


draw_h(t, 100)

def draw_i(t, length):
    lr(t1, length)
    t1.lt(180)
    lr(t1, length*.5)
    t1.lt(90)
    t1.fd(length)
    move(t1, 0, -100)
    t1.lt(90)
    t1.fd(length)
    reset(t)
    

draw_i(t, 100)

def draw_j(t, length):
    lr(t1, length)
    t1.lt(180)
    lr(t1, length*.5)
    t1.lt(90)
    t1.fd(length*.8)
    arc(t1, 25, -90)
    arc(t1, 25, -90)
    reset(t)

draw_j(t, 100)


def draw_k(t, length):
    t1.lt(270)
    t1.fd(length)
    move(t2, 33, 0)
    t2.lt(240)
    t2.fd(length*.7)
    t2.lt(90)
    t2.fd(length*.7)
    t1.reset()
    t2.reset()
    

draw_k(t, 100)


def draw_l(t, length):
    t1.lt(270)
    t1.fd(length)
    t1.lt(90)
    t1.fd(length*.5)
    t1.reset()


draw_l(t, 100)

def draw_m(t, length):
    t1.lt(75)
    t1.fd(length*1.1)
    t1.rt(135)
    t1.fd(length*1.2)
    t1.lt(135)
    t1.fd(length*1.2)
    t1.rt(135)
    t1.fd(length*1.3)
    reset(t)

draw_m(t, 100)



def draw_n(t, length):
    down(t1, length)
    move(t1, 0, 0)
    t1.lt(45)
    t1.fd(length*1.35)
    t1.lt(135)
    t1.fd(length)
    reset(t)


draw_n(t, 100)



def draw_o(t, length):
    circle(t1, 50)
    

draw_o(t1, 100)
reset(t1)


def draw_p(t, length):
    t1.lt(270)
    t1.fd(length)
    arc(t2, 25, -90)
    arc(t2, 25, -90)
    reset(t)

draw_p(t, 100)




def draw_q(t, length):
    draw_o(t1, length)
    move(t1, 25, 25)
    t1.rt(45)
    t1.fd(length*.4)
    reset(t)
    

draw_q(t, 100)




    
    

def draw_r(t, length):
    t1.lt(270)
    t1.fd(length)
    arc(t2, 25, -90)
    arc(t2, 25, -90)
    t2.lt(135)
    t2.fd(length*.7)
    t1.reset()
    t2.reset()
    

draw_r(t, 100)
    


def draw_s(t, length):
    arc(t1, 25, 90)
    arc(t1, 25, 90)
    arc(t1, 25, -90)
    arc(t1, 25, -90)

    t1.reset()


draw_s(t, 100)


def draw_t(t, length):
    lr(t1, length)
    t1.lt(180)
    lr(t1, length*.5)
    t1.lt(90)
    t1.fd(length)
    reset(t)

draw_t(t, 100)
    


def draw_u(t, length):
    down(t1, length*.7)
    arc(t1, 25, 90)
    arc(t1, 25, 90)
    t1.fd(length*.7)
    reset(t)

draw_u(t, 100)



def draw_v(t, length):
    t1.lt(75)
    t1.fd(length)
    t2.lt(105)
    t2.fd(length)


draw_v(t, 100)
reset(t)



def draw_w(t, length):
    t1.lt(285)
    t1.fd(length*1.1)
    t1.lt(135)
    t1.fd(length*1.2)
    t1.rt(135)
    t1.fd(length*1.2)
    t1.lt(135)
    t1.fd(length*1.3)
    reset(t)

draw_w(t, 100)

    

def draw_x(t, length):

    t1.penup()
    t1.goto(-25, 0)
    t1.pendown()
    t1.lt(75)
    t1.fd(length)
    t2.lt(105)
    t2.fd(length)
    t1.reset()
    t2.reset()

draw_x(t, 100)


def draw_y(t, length):
    draw_v(t1, length*.6)
    down(t3, length*.6)
    reset(t1)
    reset(t2)
    
draw_y(t1, 100)

def draw_z(t, length):
    lr(t1, length)
    t1.rt(135)
    t1.fd(length*1.3)
    t1.lt(135)
    t1.fd(length)
    reset(t)
    

draw_z(t, 100)


