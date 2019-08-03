from turtle import *
ht()

T=[
    [0,1,0],
    [1,0,0],
    [1,1,1]
]



def square():
    pen(fillcolor="black", pencolor="black", pensize=1)
    
    begin_fill()
    pd()
    for i in range(4):
        forward(2)
        right(90)
    
    pu()

    end_fill()
def rep(T):
    ht()
    tracer(100)
    pu()
    left(90)
    for i in T:
        for j in i:
            if j==1:
                square()   
            right(90)
            forward(4)
            left(90)
        left(90)
        for j in i:
            forward(4)
        left(90)
        forward(4)
        right(180)


rep(T)