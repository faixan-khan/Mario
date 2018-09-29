import main
from mainobj import *
class Bricks(objects):
    def __init__(self,x,y,stri):
        objects.__init__(self,x,y)
        self.str=stri
    def blit(self):
        main.board[self.x][self.y]=self.str