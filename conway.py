import time
import random

class Row():
    def __init__(self,n):
        self.dat=[0 for i in range(n)]
        self.n=n
    def __getitem__(self, i):
        return self.dat[i%self.n]
    def __setitem__(self,i, k):
        self.dat[i%self.n]=k
    def __iter__(self):
        return iter(self.dat)
    def __len__(self):
        return self.n
    def __str__(self):
        d=[i for i in self.dat]
        
        for c,i in enumerate(d):
            if i==1:
                d[c]='X'
            else:
                d[c]=' '
        ret='| '
        ret+=' | '.join(d)
        ret+=' |'
        return ret
class Table():
    def __init__(self,n):
        
        tab=[Row(n) for i in range(n)]
        self.tab=tab
        self.n=n
    def __str__(self):
        line='----'
        line*=self.n
        line+='-\n'
        rep=[line]
        for i in self.tab:
            rep.append(str(i)+'\n')
            rep.append(line)
        return ''.join(rep)
    def __repr__(self):
        rep=[]
        for i in self.tab:
            
            rep.append(str(i)+'\n')
        return ''.join(rep)
    def __iter__(self):
        return iter(self.tab)
    def __eq__(self,other):
        for c, i in enumerate(self.tab):
            for d, j in enumerate(i):
                if j!=other.tab[c][d]:
                    return False
        return True
    def __len__(self):
        return self.n
    def __abs__():
        return self.n**2
    def __getitem__(self,i):

        return self.tab[i%self.n]
    def consume(self,T):
        for c in range(self.n):
            for k in range(self.n):
                self[c][k]=T[c][k]
    def alive(self,i,j):
        if self[i][j]==1:
            return True
        else:
            return False
    def neighbours(self,i,j):
        """
        return the number of alive neighborurs
        """
        L=[
            self[i-1][j-1],
            self[i-1][j],
            self[i-1][j+1],
            self[i][j-1],
            self[i][j+1],
            self[i+1][j-1],
            self[i+1][j],
            self[i+1][j+1]
        ]
        return L.count(1)

    def willive(self,i,j):
        """
        checks the number of neighbours to see if the cell will live/get born

        """
        nei=self.neighbours(i,j)
        if self.alive(i,j):
            if 2<nei<5:
                return True
            else:
                return False
        else:
            if nei!=3:
                return False
            else:
                return True
    def age(self):
        baby=Table(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if self.willive(i,j):
                    baby[i][j]=1
        return baby
    def paint(self,x,y):
        global pause
        n=self.n
        if x//10<n and y//10<n:
            if pause:
                pause=False
                
            else:
                pause=True




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
    right(180)
    for i in range(4):
        forward(8)
        left(90)
    right(180)
    pu()

    end_fill()
def rep(T):
    pu()
    tracer(0,0)
    goto(0,0)
    setheading(90)
    for i in T:
        for j in i:
            
            if j==1:
                square()   
            right(90)
            forward(10)
            left(90)
        left(90)
        for j in i:
            forward(10)
        left(90)
        forward(10)
        right(180)
    left(90)
    update()

pause= False
def paus():
    pause= True
    if pause:
        pause= False
        
    else:
        pause= True
def main(n):
     
    screensize(n*10+50,n*10+50)
    setworldcoordinates(0,-n*10-50,n*10+50,0)
    
    m=Table(n)
    
    T=[[random.randint(0,1) for i in range(n)] for j in range(n)] 
    
    m.consume(T)
    screen=Screen()
    screen.onkey(paus, "Up")
    screen.listen()
    while m!=m.age() and m!=m.age().age():
        
        clear()
        ht()
        
        m=m.age()
        rep(m)
        time.wait(0.5)
        

    rep(m)
    time.sleep(2)
    




def main2():
    rep(T)
if __name__=='__main__':
    main(20)








"""
Infinite ones:
   T=[
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
"""