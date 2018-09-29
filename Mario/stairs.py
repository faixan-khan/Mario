import main
from mainobj import *
from originalenemy import *
class stair(originalenemy):
    def __init__(self,x,y,stri,stri2):
        objects.__init__(self,x,y)
        self.str=stri
        self.stri=stri2
        self.speed=1
        self.life=1
    def sety(self,y):
        self.y=y
    def setx(self,x,y):
        if main.board[self.x+self.speed][self.y] == '   ' and self.x > 2 and self.x <= 6:
            self.x=x+self.speed
        elif main.board[self.x+self.speed][self.y] == '   ':
            self.x=3