import main
from mainobj import *
class originalenemy():
    def __init__(self,x,y):
        objects.__init__(self,x,y)
        self.speed=1
        self.life=1
    def show(self):
        main.board[self.x][self.y]=self.str
        main.board[self.x-1][self.y]=self.stri
    def remove(self,x,y):
        main.board[x][y]="   "
        main.board[x-1][y]="   "


   