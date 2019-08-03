import time
import random
import pygame
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
    def __abs__(self):
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
            if 1<nei<4:
                return True
            else:
                return False
        else:
            if nei==3:
                return True
            else:
                return False
    def age(self):
        baby=Table(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if self.willive(i,j):
                    baby[i][j]=1
        return baby
    def paint(self,y,x):
        self[y][x]=(self[y][x]+1)%2



def create_grid(Tab,size):
    ret=[]
    for c, i in enumerate(Tab):
        ret.append([])
        for k, j in enumerate(i):
            ret[c].append(pygame.Rect(k*size, c*size,size-2,size-2))
    return ret
def update_grid(Tab, Grid,screen):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    for c, i, in enumerate(Tab):
        for k,j in enumerate(i):
            if j==1:
                pygame.draw.rect(screen, BLACK,Grid[c][k], 0 )
            else:
                pygame.draw.rect(screen, WHITE,Grid[c][k], 0 )
def button(screen, y, colour, n, s):
    pygame.draw.rect(screen,colour,(n*s+25,y,50,50),0)
    pygame.display.update(n*s+25,y,50,50)

def paused(grid, screen,clock,m, s, n, speed):
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    pause=True
    update_grid(m,grid,screen)
    pygame.display.update(0,0,s*n,s*n)
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:    
                pause=False    
            if event.type == pygame.MOUSEBUTTONUP:
                
                x,y =pygame.mouse.get_pos()
                if x<s*n and y<s*n:
                    x=x//s
                    y=y//s

                    m.paint(y, x)
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 10<=y<=50 and n*s+25<x:
                    if speed ==10:
                        speed=1
                        button(screen,10,GREEN,n,s)
                    else:
                        speed=10
                        button(screen,10,RED,n,s)
                if  100<=y<=150 and n*s+25<x:
                    T=[[random.randint(0,1) for i in range(n)] for j in range(n)] 
                    m.consume(T)
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 190<=y<=240 and n*s+25<x:
                    m=m.age()
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 280<=y<=330 and n*s+25<x:
                    T=[[0 for i in range(n)] for j in range(n)]
                    m.consume(T)
                    update_grid(m,grid, screen)
                    pygame.display.update(0,0,s*n,s*n)
        clock.tick(15)  
    return speed
def randmtb(n):
    return [[random.randint(0,1) for i in range(n)] for j in range(n)] 


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

def main(n,s):
     

 
    # Initialize the game engine
    pygame.init()
    
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
 
    PI  = 3.141592653
    
    # Set the height and width of the screen
    size = (n*s+100, n*s)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Conway's game of life")
    
    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    speed=10
    button(screen,10,RED,n,s)
    button(screen,100,BLUE,n,s)
    button(screen,190,(255,255,0),n,s)
    button(screen,280,WHITE,n,s)
    #table of size n
    m=Table(n)
    #creating a random spread of 1s and 0s
    T=randmtb(n)
    #updating the table
    m.consume(T)
    grid=create_grid(m,s)
    # Loop as long as done == False
    while not done:
        # Clear the screen and set the screen background
        screen.fill(WHITE)
        update_grid(m,grid,screen)
        
        
        
            # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.update(0,0,s*n,s*n)
        if m==m.age() or m==m.age().age():
            m.consume(randmtb(n))
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        # All drawing code happens after the for loop and but
        # inside the main while not done loop.
            if event.type == pygame.KEYDOWN:
                speed=paused(grid, screen, clock,m, s, n, speed)
            if event.type == pygame.MOUSEBUTTONUP:
                
                x,y =pygame.mouse.get_pos()
                if x<s*n and y<s*n:
                    x=x//s
                    y=y//s

                    m.paint(y, x)
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 10<=y<=50 and n*s+25<x:
                    if speed ==10:
                        speed=1
                        button(screen,10,GREEN,n,s)
                    else:
                        speed=10
                        button(screen,10,RED,n,s)
                if  100<=y<=150 and n*s+25<x:
                    T=[[random.randint(0,1) for i in range(n)] for j in range(n)] 
                    m.consume(T)
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 190<=y<=240 and n*s+25<x:
                    m=m.age()
                    update_grid(m,grid,screen)
                    pygame.display.update(0,0,s*n,s*n)
                if 280<=y<=330 and n*s+25<x:
                    T=[[0 for i in range(n)] for j in range(n)]
                    m.consume(T)
                    update_grid(m,grid, screen)
                    pygame.display.update(0,0,s*n,s*n)
        
        m=m.age()
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        
        clock.tick(speed)
 
    # Be IDLE friendly
    pygame.quit()


    
if __name__=='__main__':
    main(100, 10)








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