import main
from mainobj import *
from originalenemy import *
class enemy(originalenemy):
    def __init__(self,x,y,stri,stri2):
        objects.__init__(self,x,y)
        self.str=stri
        self.stri=stri2
        self.speed=1
        self.life=1
    def setx(self,x):
        self.x=x
    def sety(self,x,y):
        turn = 0
        if main.board[self.x][self.y+self.speed] == '   ':
            self.y=y+self.speed
        elif main.board[self.x][self.y+self.speed] != '   ':
            self.speed=-1*self.speed
            self.y=y+self.speed