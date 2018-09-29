import random
import sys
import os
import time
import NonBlockingInput as keyb
board=[]
brick=[]
pipe=[]
kb=keyb.KBHit()
start=0
end=36
score=0
pipehit=0
def drawboard(start,end):
	hori = '|=============================================================================================================|'
	HLINE = '--+---+---+---+---+---+---+---+---+---+---+---+--+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--'
	print(HLINE)
	for x in range(15):
		print('|',end =' ')
		for y in range(start,end):
			print('%s' % (board[x][y]),end ='')
		print('|')
	for i in range(6):
		print(hori)
def getnewboard():
	for i in range(36):
		board.append(['   ']*500)
	return board
def resetboard(start,end):
	for x in range(15):
		for y in range(start,end):
			board[x][y]='  '
class character:
	def __init__(self,x,y,stri):
		self.x = x
		self.y = y
		self.str=stri
	def blit(self):
		board[self.x][self.y]=self.str
class Bricks(character):
	def __init__(self,x,y,str):
		character.__init__(self,x,y,str)
	def blit(self):
		board[self.x][self.y]=self.str
class mario(character):
	def __init__(self,x,y,stri):
		self.x=x
		self.y=y
		self.str=stri
	def show(self):
		board[self.x][self.y]=self.str
	def setx(self,x):
		self.x=x
	def sety(self,y):
		self.y=y
	def remove(self,x,y):
		board[x][y]="   "
def kill(x,y,xe,ye):
	kill=0
	if ye==y and xe==x+1:
		kill=1
	else:
		kill=0
	return kill
def pipe_hit(xe,ye):
	pipehit=0
	if ye >= end and ye < start:
		if board[ye-1] != "   ":
			pipehit = -1
		if board[ye+1] != "   ":
			pipehit = 1
	return
def collision(x,y,xe,ye):
	ans=0
	if ye==y and xe==x:
		ans = 1
	else:
		ans = 0
	pipe_hit(xe,ye)
	return ans
			
gameboard=getnewboard()
brick=[[11,4],[11,5],[11,6],[7,7],[7,8],[11,13],[11,14],[11,15],[11,25],[11,26],[11,27],[7,28],[7,29],[7,30],[7,31],[9,60],[9,61],[9,98],[9,110],[9,114],[9,115],[12,33],[12,59],[12,108],[12,97],[12,111]]
coins=[[10,5],[10,15],[6,28],[6,30],[8,60],[8,62],[8,98],[8,110],[9,114]]
power=[[6,8]]
pipe=[[14,33],[13,33],[14,59],[13,59],[14,108],[13,108],[14,97],[13,97],[14,111],[13,111]]
#enemy=[[14,32],[14,56],[14,70],[14,95],[14,105],[14,109]]
for i in brick:
	b=Bricks(i[0],i[1],"___")
	b.blit()
for i in coins:
	c=Bricks(i[0],i[1],"$$$")
	c.blit()
for i in power:
	p=Bricks(i[0],i[1],"PUP")
	p.blit()
for i in pipe:
	p=Bricks(i[0],i[1],"| |")
	p.blit()


x=14
y=0
xe1=14
ye1=30
xe2=14
ye2=31
xe3=14
ye3=38
m=mario(x,y,"!.!")
e1=mario(xe1,ye1,"(^)")
e2=mario(xe2,ye2,"(^)")
e3=mario(xe3,ye3,"(^)")
flag=0
abgrnd=0
lives=3
enloc=0
kills=0
size=0
while(1):
	enloc=enloc+1
	col1=0
	col2=0
	col3=0
	os.system('clear')
	drawboard(start,end)
	m.show()
	e1.show()
	e2.show()
	e3.show()
	if kb.kbhit():
		char=kb.getch()
	else:
		char="{"
	if char == "d" and board[x][y+1] ==  '   ':
		m.remove(x,y)
		m.sety(y+1)
		y=y+1
		m.show()
		if y > (start+end)/2:
			start=start+1
			end=end+1
	if char == "d":
		if board[x][y+1] == '$$$':
			score=score+1
			m.remove(x,y)
			m.sety(y+1)
			y=y+1
			m.show()
		elif board[x][y+1] == "PUP":
			m.remove(x,y)
			m.remove(x,y)
			m.sety(y+1)
			y=y+1
			m.show()
			size=1
		elif board[x][y+1] == "(^)":
			if lives>0:
				m.remove(x,y)
	if size==1:
		m=mario(x,y,"!O!")
	if size==0:
		m=mario(x,y,"!o!")
	if char == "a" and board[x][y-1] == '$$$':
		score=score+1
		m.remove(x,y)
		m.sety(y-1)
		y=y-1
		m.show()
	if char == "a" and board[x][y-1]=='   ':
		if y > start:
			m.remove(x,y)
			m.sety(y-1)
			y=y-1
			m.show()

	if char == "w" and flag==0 and board[x-1][y] == '   ':
		flag=1
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
	elif flag==1 and board[x-1][y] == '   ':
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
		flag=2
	elif flag==2 and board[x-1][y] == '   ':
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
		flag=3
	elif flag==3 and board[x-1][y] == '   ':
		flag=4
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
	elif flag==4:
		if board[x+1][y] == '___':
			m.remove(x,y)
			m.show()
			abgrnd=1
			flag=0
		else:
			flag=5
			m.remove(x,y)
			m.setx(x=x+1)
			x=x+1
			m.show()
	elif flag==5 or flag==3:
		if board[x+1][y]!='   ':
			m.remove(x,y)
			m.show()
			abgrnd=1
			flag=0
		else:
			flag=6
			m.remove(x,y)
			m.setx(x=x+1)
			x=x+1
			m.show()
	elif flag==6 or flag==2:
		flag=7
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
	elif flag==7 or flag==1:
		flag=0
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
		if board[x+1][y]=='   ':
			flag=14-x
	elif board[x+1][y] == '___' and x < 14 and abgrnd == 1:
		flag = 0

	elif x==14:
		abgrnd=0
		flag=0
	elif flag==4 and abgrnd==1 and board[x+1][y]=='   ':
		abgrnd=0
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
		if board[x+1][y]=='___':
			abgrnd=0
			flag=0
	
	elif board[x+1][y]=='   ':
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
	elif board[x+1][y]=='(^)':
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
	if enloc==6:	
		col1=collision(x,y,xe1,ye1)
		kills=kill(x,y,xe1,ye1)
		if col1==0 and kills==0:
    		e1.remove(xe1,ye2)
			e1.sety(ye1-1)
			ye1=ye1-1
			e1.show()
		if col1==1 and kills==0:
    		if size==1:
				size=0
			else:
				lives=lives-1
			e1.remove(xe1,ye1)
			e1.sety(ye1-1)
			ye1=ye1-1
			e1.show()
			col1=0
		elif col1==1 and kills==1:
			e1.remove()
			score=score+1
			kill=0
		col2=collision(x,y,xe2,ye2)
		kills=kill(x,y,xe2,ye2)
		if col2==0 and kills==0:
    		e2.remove(xe2,ye2)
			e2.sety(ye2-1)
			ye2=ye2-1
			e2.show()
		if col2==1 and kills==0:
    		if size==1:
				size=0
			else:
				lives=lives-1
			e2.remove(xe2,ye2)
			e2.sety(ye2-1)
			ye2=ye2-1
			e2.show()
			col2=0
		elif col2==1 and kills==1:
			e2.remove()
			score=score+1
			kill=0
		col3=collision(x,y,xe3,ye3)
		kills=kill(x,y,xe3,ye3)
		if col3==0 and kills==0:
    		e3.remove(xe3,ye3)
			e3.sety(ye3-1)
			ye3=ye3-1
			e3.show()
		if ye3 > start and ye3 < end:
			if col3==1 and kills==0:
				if size==1:
					size=0
				else:
					lives=lives-1
				if pipehit == 0:
					e3.remove(xe3,ye3)
					e3.sety(ye3-1)
					ye3=ye3-1
					e3.show()
					col3=0
				elif pipehit == -1:
					e3.remove(xe3,ye3)
					e3.sety(ye3+1)
					ye3=ye3+1
					e3.show()
					col3=0
				elif pipehit == 1:
					e3.remove(xe3,ye3)
					e3.sety(ye3-1)
					ye3=ye3-1
					e3.show()
					col3=0
			elif col3==1 and kills==1:
				e3.remove()
				score=score+1
				kill=0
		enloc=0
	print(score)
	print(flag)
	print(lives)
	if lives<0:
		break
	time.sleep(0.070)
