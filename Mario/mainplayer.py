import main
from mainobj import *
class mario():
	def __init__(self,x,y,stri):
		objects.__init__(self,x,y)
		self.str=stri
	def show(self):
		main.board[self.x][self.y]=self.str
	def setx(self,x):
		self.x=x
	def sety(self,y):
		self.y=y
	def remove(self,x,y):
		main.board[x][y]="   "