import random
import sys
import os
import time
import NonBlockingInput as keyb
from mainplayer import *
import main
import bricks as bric
from enemy import *
from bossenemy import *
from stairs import *
from colors import *
import termios
import sys,tty

colors=bcolors()
cunt=0
brick=[]
pipe=[]
kb=keyb.KBHit()
start=0
end=36
score=0
invinsible=0
stair_count=0
stars_count=0
m=mario(14,0,colors.PURPLE +'!o!'+ bcolors.ENDC)

def drawboard(start,end):
	hori = '|=============================================================================================================|'
	HLINE = '--+--+---+---+---+---+---+---+---+---+---+---+---+--+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--'
	print(HLINE)
	for x in range(15):
		print('|',end =' ')
		for y in range(start,end):
			print('%s' % (main.board[x][y]),end ='')
		print('|')
	for i in range(6):
		print(hori)

def userinput():
	old = termios.tcgetattr(sys.stdin)
	tty.setcbreak(sys.stdin.fileno())
	try:
		key = sys.stdin.read(1)
	except:
		pass
	return key
def pause():
	print("You have paused the game. Press 'p' to restart")
	while(1):
		c = userinput()
		if c == 'p':
			break

def getnewboard():
	for i in range(36):
		main.board.append(['   ']*320)
	return main.board

def resetboard(start,end):
	for x in range(15):
		for y in range(start,end):
			main.board[x][y]='  '
			
gameboard=getnewboard()

brick=[[12,260],[11,255],[12,290],[11,4],[11,5],[11,6],[7,7],[7,8],[11,13],[11,14],[11,15],[11,25],[11,26],[11,27],[7,28],[7,29],[7,30],[7,31],[11,40],[11,41],[7,42],[7,43],[9,60],[9,61],[12,66],[9,98],[11,101],[9,110],[9,114],[9,115],[12,33],[12,59],[12,108],[12,97],[12,111],[12,125],[12,129],[12,133],[12,127],[12,131],[12,135],[11,150],[11,151],[11,152],[7,154],[7,155],[7,156],[4,158],[4,159],[4,160],[3,161],[3,164],[11,166],[13,200],[12,202],[11,205],[11,206],[7,208],[7,209],[4,211],[7,215],[7,216],[11,218],[11,219],[11,220],[11,221],[11,222],[7,224],[7,225],[4,227]]

coins=[[10,5],[10,15],[6,28],[6,30],[8,60],[8,62],[8,67],[8,69],[8,98],[10,40],[8,110],[9,114]]

pipe=[[14,260],[13,260],[14,290],[13,290],[14,33],[13,33],[14,59],[13,59],[14,66],[13,66],[14,108],[13,108],[14,97],[13,97],[14,111],[13,111],[14,127],[13,127],[14,131],[13,131],[14,135],[13,135],[14,161],[13,161],[12,161],[11,161],[10,161],[9,161],[8,161],[7,161],[6,161],[5,161],[4,161],[14,164],[13,164],[12,164],[11,164],[10,164],[9,164],[8,164],[7,164],[6,164],[5,164],[4,164],[14,200],[14,202],[13,202],[14,211],[13,211],[12,211],[11,211],[10,211],[9,211],[8,211],[7,211],[6,211],[5,211],[14,227],[13,227],[12,227],[11,227],[10,227],[9,227],[8,227],[7,227],[6,227],[5,227]]

st=[]
stars=[260,261,262,263,264,265,266]

star=[]
tarey=[297,298,299,300,301]

en=[]
coEn=[31,40,44,76,77,109,128,133,157,175,179,183,187,191,195,212,215,218,221,224]

ben=[]
boEn=[210]

for j in range(0,1):
		be=bossenemy(14,boEn[j],"/^\\","^o^")
		ben.append(be)

for i in range(0,20):
	e=enemy(14,coEn[i],colors.ORANGE +"(^)"+ bcolors.ENDC,colors.ORANGE +"*o*"+ bcolors.ENDC)
	en.append(e)

for i in range(0,7):
	ta=stair(5,stars[i],colors.YELLOW +" ☆彡"+ bcolors.ENDC,"   ")
	st.append(ta)

for i in range(0,5):
	tr=stair(5,tarey[i],colors.YELLOW +" ☆ "+ bcolors.ENDC,"   ")
	star.append(tr)

def kill(x,y,xe,ye):
	global kills
	for i in en:
		if x+2 == i.x and y == i.y:
			i.life = -1
			kills = 1
			global cunt
			cunt=cunt+1
		else:
			kills=0
		
	return kills
def killboss(x,y,xe,ye):
	global killbo
	for j in ben:
		if x+2 == j.x and y == j.y:
			j.life = j.life - 1
			killbo = 1
		else:
			killbo=0
    			

def collision(x,y,xe,ye):
	ans=0
	if xe==x and ye==y+1:
		ans = 1
	elif xe==x and ye==y-1:
		ans = 1
	else:
		ans = 0
	return ans

for i in brick:
	b=bric.Bricks(i[0],i[1],"___")
	b.blit()

for i in coins:
	c=bric.Bricks(i[0],i[1],"$$$")
	c.blit()

for i in pipe:
	p=bric.Bricks(i[0],i[1],"| |")
	p.blit()


x=14
y=0
nonflag=0
flag=0
abgrnd=0
lives=3
enloc=0
global killed
killed=0
global killedboss
killedboss=0
size=0
ck=1
invinsible_y=0
timer=2000
bossen=0
print("INSTRUCTIONS")
print("press D for moving forward")
print("press A for moving backward")
print("press W to jump")
print("PUP is power up")
print("UCL makes the enemies disappear for a short period")
print("ENTER YOUR NAME")
nameTH=input()
print(nameTH)
if nameTH:
	true=1

while(true==1):
	timer=timer-1
	enloc=enloc+1
	col1=0
	col2=0
	os.system('clear')
	print()
	print("LIVES :",lives)
	print(nameTH+"'s","SCORE :",score)
	print("ENEMIES KILLED :",cunt)
	print("TIMER :",timer)
	

	drawboard(start,end)
	main.board[x][y]='   '
	m.show()
	
	main.board[2][16]='   '
	main.board[2][17]='__ '
	main.board[2][18]='  _'
	main.board[3][16]=' _('
	main.board[3][17]='  )'
	main.board[3][18]='_( '
	main.board[3][19]=')_ '
	main.board[4][16]='(_ '
	main.board[4][17]='  _'
	main.board[4][18]='   '
	main.board[4][19]=' _)'
	main.board[5][16]='  ('
	main.board[5][17]='_) '
	main.board[5][18]='(__'
	main.board[5][19]=')  '

	main.board[2][47]='   '
	main.board[2][48]='__ '
	main.board[2][49]='  _'
	main.board[3][47]=' _('
	main.board[3][48]='  )'
	main.board[3][49]='_( '
	main.board[3][50]=')_ '
	main.board[4][47]='(_ '
	main.board[4][48]='  _'
	main.board[4][49]='   '
	main.board[4][50]=' _)'
	main.board[5][47]='  ('
	main.board[5][48]='_) '
	main.board[5][49]='(__'
	main.board[5][50]=')  '

	main.board[2][72]='   '
	main.board[2][73]='__ '
	main.board[2][74]='  _'
	main.board[3][72]=' _('
	main.board[3][73]='  )'
	main.board[3][74]='_( '
	main.board[3][75]=')_ '
	main.board[4][72]='(_ '
	main.board[4][73]='  _'
	main.board[4][74]='   '
	main.board[4][75]=' _)'
	main.board[5][72]='  ('
	main.board[5][73]='_) '
	main.board[5][74]='(__'
	main.board[5][75]=')  '

	main.board[2][83]='   '
	main.board[2][84]='__ '
	main.board[2][85]='  _'
	main.board[3][83]=' _('
	main.board[3][84]='  )'
	main.board[3][85]='_( '
	main.board[3][86]=')_ '
	main.board[4][83]='(_ '
	main.board[4][84]='  _'
	main.board[4][85]='   '
	main.board[4][86]=' _)'
	main.board[5][83]='  ('
	main.board[5][84]='_) '
	main.board[5][85]='(__'
	main.board[5][86]=')  '

	main.board[1][131]='   '
	main.board[1][132]='   '
	main.board[1][133]='   '
	main.board[1][134]=' .-'
	main.board[1][135]='~~~'
	main.board[1][136]='-. '
	main.board[2][131]='  .'
	main.board[2][132]='- ~'
	main.board[2][133]=' ~-'
	main.board[2][134]='(  '
	main.board[2][135]='   '
	main.board[2][136]='  )'
	main.board[2][137]='_ _'
	main.board[3][131]=' / '
	main.board[3][132]='   '
	main.board[3][133]='   '
	main.board[3][134]='   '
	main.board[3][135]='   '
	main.board[3][136]='   '
	main.board[3][137]='   '
	main.board[3][138]='  ~'
	main.board[3][139]=' -.'
	main.board[4][131]='|  '
	main.board[4][132]='   '
	main.board[4][133]='   '
	main.board[4][134]='   '
	main.board[4][135]='   '
	main.board[4][136]='   '
	main.board[4][137]='   '
	main.board[4][138]='   '
	main.board[4][139]='   '
	main.board[4][140]=' \ '
	main.board[5][131]=' \ '
	main.board[5][132]='   '
	main.board[5][133]='   '
	main.board[5][134]='   '
	main.board[5][135]='   '
	main.board[5][136]='   '
	main.board[5][137]='   '
	main.board[5][138]='   '
	main.board[5][139]='   '
	main.board[5][140]='.  '
	main.board[6][131]='   '
	main.board[6][132]='~- '
	main.board[6][133]='. _'
	main.board[6][134]='___'
	main.board[6][135]='___'
	main.board[6][136]='___'
	main.board[6][137]='___'
	main.board[6][138]=' . '
	main.board[6][139]='-~ '

	main.board[3][305]='   '
	main.board[3][306]='   '
	main.board[3][307]='   '
	main.board[3][308]='   '
	main.board[3][309]='.-.'
	main.board[4][305]='   '
	main.board[4][306]='   '
	main.board[4][307]='   '
	main.board[4][308]='  ('
	main.board[4][309]='/^\\'
	main.board[4][310]=')  '
	main.board[5][305]='   '
	main.board[5][306]='   '
	main.board[5][307]='   '
	main.board[5][308]='  ('
	main.board[5][309]='\ /'
	main.board[5][310]=')  '
	main.board[6][305]='   '
	main.board[6][306]='   '
	main.board[6][307]='   '
	main.board[6][308]='  .'
	main.board[6][309]='-`-'
	main.board[6][310]='.  '
	main.board[7][305]='   '
	main.board[7][306]='   '
	main.board[7][307]='   '
	main.board[7][308]=' /('
	main.board[7][309]='_I_'
	main.board[7][310]=')\ '
	main.board[8][305]='   '
	main.board[8][306]='   '
	main.board[8][307]='   '
	main.board[8][308]=' \\'
	main.board[8][309]=') ('
	main.board[8][310]='// '
	main.board[9][305]='   '
	main.board[9][306]='   '
	main.board[9][307]='   '
	main.board[9][308]='  /'
	main.board[9][309]='   '
	main.board[9][310]='\  '
	main.board[10][305]='   '
	main.board[10][306]='   '
	main.board[10][307]='   '
	main.board[10][308]='  |'
	main.board[10][309]='   '
	main.board[10][310]='|  '
	main.board[11][305]='   '
	main.board[11][306]='   '
	main.board[11][307]='   '
	main.board[11][308]='  |'
	main.board[11][309]='___'
	main.board[11][310]='|  '
	main.board[12][305]='   '
	main.board[12][306]='   '
	main.board[12][307]='   '
	main.board[12][308]='   '
	main.board[12][309]='/|\\'
	main.board[13][305]='   '
	main.board[13][306]='   '
	main.board[13][307]='   '
	main.board[13][308]='   '
	main.board[13][309]='\\|/'
	main.board[14][305]='   '
	main.board[14][306]='   '
	main.board[14][307]='   '
	main.board[14][308]='   '
	main.board[14][309]='/Y\\'

	main.board[5][310]="Tha"
	main.board[5][311]="nk "
	main.board[5][312]="you"
	main.board[5][313]=" Ma"
	main.board[5][314]="rio"

	if y > 115 and start > 100:
		main.board[7][115]=colors.PURPLE + 'PRO' + bcolors.ENDC
		main.board[7][116]=colors.PURPLE + 'CEE'+ bcolors.ENDC
		main.board[7][117]=colors.PURPLE + 'D T'+ bcolors.ENDC
		main.board[7][118]=colors.PURPLE + 'O P'+ bcolors.ENDC
		main.board[7][119]=colors.PURPLE + 'LAY'+ bcolors.ENDC
		main.board[7][120]=colors.PURPLE + ' LE'+ bcolors.ENDC
		main.board[7][121]=colors.PURPLE + 'VEL'+ bcolors.ENDC
		main.board[7][122]=colors.PURPLE + ' :2'+ bcolors.ENDC
	
	if y > 160 and start > 160:
		main.board[10][169]='/ ^'
		main.board[10][170]='   '
		main.board[10][171]='^  '
		main.board[10][172]=' ^ '
		main.board[10][173]='   '
		main.board[10][174]='^  '
		main.board[10][175]='||_'
		main.board[10][176]='__|'
		main.board[10][177]='___'
		main.board[10][178]='|||'
		main.board[10][179]='|||'
		main.board[10][181]='|||'
		main.board[10][182]='|||'
		main.board[10][183]='___'
		main.board[10][184]='|__'
		main.board[10][185]='|||'
		main.board[10][186]='   '
		main.board[10][187]='   '
		main.board[10][188]=' | '
		main.board[10][189]='|  '
		main.board[9][169]=' /^'
		main.board[9][170]='^  '
		main.board[9][171]='^ ^'
		main.board[9][172]='^  '
		main.board[9][173]='^  '
		main.board[9][174]='  |'
		main.board[9][175]='|__'
		main.board[9][176]='_|_'
		main.board[9][177]='__|'
		main.board[9][178]='|||'
		main.board[9][179]='|||'
		main.board[9][180]='|||'
		main.board[9][181]='||_'
		main.board[9][182]='__|'
		main.board[9][183]='__|'
		main.board[9][184]='|| '
		main.board[9][185]='   '
		main.board[9][186]='  /'
		main.board[9][187]='||o'
		main.board[9][188]='|||'
		main.board[9][189]='|||'
		main.board[9][190]='\  ' 
		main.board[8][169]='  /'
		main.board[8][170]='  ^'
		main.board[8][171]='  ^'
		main.board[8][172]='^ ^'
		main.board[8][173]=' ^ '
		main.board[8][174]=' /_'
		main.board[8][175]='___'
		main.board[8][176]='___'
		main.board[8][177]='___'
		main.board[8][178]='___'
		main.board[8][179]='___'
		main.board[8][180]='___'
		main.board[8][181]='___'
		main.board[8][182]='___'
		main.board[8][183]='___'
		main.board[8][184]='___'
		main.board[8][185]='_\ '
		main.board[8][186]=' ^ '
		main.board[8][187]=' /|'
		main.board[8][188]='|||'
		main.board[8][189]='|o|'
		main.board[8][190]='\  '
		main.board[7][169]='   '
		main.board[7][170]='/ ^'
		main.board[7][171]='^  '
		main.board[7][172]='^ ^'
		main.board[7][173]=' ^\\'
		main.board[7][174]='  /'
		main.board[7][175]='___'
		main.board[7][176]='___'
		main.board[7][177]='___'
		main.board[7][178]='___'
		main.board[7][179]='___'
		main.board[7][180]='___'
		main.board[7][181]='___'
		main.board[7][182]='___'
		main.board[7][183]='___'
		main.board[7][184]='___'
		main.board[7][185]='\ ^'
		main.board[7][186]=' ^ '
		main.board[7][187]='  /'
		main.board[7][188]='|o|'
		main.board[7][189]='||\\'
		main.board[6][169]='   '
		main.board[6][170]=' / '
		main.board[6][171]='^ ^'
		main.board[6][172]='  ^'
		main.board[6][173]=' \ '
		main.board[6][174]='^  '
		main.board[6][175]='_\_'
		main.board[6][176]='___'
		main.board[6][177]='___'
		main.board[6][178]='___'
		main.board[6][179]='___'
		main.board[6][180]='___'
		main.board[6][181]='___'
		main.board[6][182]='|  '
		main.board[6][183]='|__'
		main.board[6][184]='___'
		main.board[6][185]='^ ^'
		main.board[6][186]='   '
		main.board[6][187]='   '
		main.board[6][188]='/||'
		main.board[6][189]='o\ '
		main.board[5][169]='   '
		main.board[5][170]='  /'
		main.board[5][171]='  ^'
		main.board[5][172]=' ^ '
		main.board[5][173]='\/^'
		main.board[5][174]='  ^'
		main.board[5][175]='\ ^'
		main.board[5][176]=' ^ '
		main.board[5][177]='^  '
		main.board[5][178]=' ^ '
		main.board[5][179]=' ^ '
		main.board[5][180]='  ^'
		main.board[5][181]='   '
		main.board[5][182]='___'
		main.board[5][183]='_  '
		main.board[5][184]='^  '
		main.board[5][185]=' ^ '
		main.board[5][186]='   '
		main.board[5][187]='   '
		main.board[5][188]=' /|'
		main.board[5][189]='\  '
		main.board[4][169]='   '
		main.board[4][170]='   '
		main.board[4][171]='/^ '
		main.board[4][172]='  \\'
		main.board[4][173]='  /'
		main.board[4][174]=' ^\\'
		main.board[3][169]='   '
		main.board[3][170]='   '
		main.board[3][171]=' / '
		main.board[3][172]='^\ '
		main.board[3][173]='   '
		main.board[3][174]='/\ '
		main.board[2][169]='   '
		main.board[2][170]='   '
		main.board[2][171]='  /'
		main.board[2][172]='\  '
		main.board[5][175]=colors.ORANGE + 'THE' + bcolors.ENDC
		main.board[5][176]=colors.ORANGE + ' PR' + bcolors.ENDC
		main.board[5][177]=colors.ORANGE + 'INC' + bcolors.ENDC
		main.board[5][178]=colors.ORANGE + 'ESS' + bcolors.ENDC
		main.board[5][179]=colors.ORANGE + ' IS' + bcolors.ENDC
		main.board[5][180]=colors.ORANGE + ' AH' + bcolors.ENDC
		main.board[5][181]=colors.ORANGE + 'EAD' + bcolors.ENDC

	if kb.kbhit():
		char=kb.getch()
	
	else:
		char="{"
	
	if main.board[x-1][y] == '___':
		if ck == 1 and y == 6:
			p=bric.Bricks(10,6,"PUP")
			p.blit()
			ck=ck+1

		if ck == 2 or ck == 1:
			if y == 41:
				p=bric.Bricks(10,41,"PUP")
				p.blit()
				ck=ck+1

		if ck == 3 or ck == 2 or ck == 1:
			if y == 101:
				p=bric.Bricks(10,101,"PUP")
				p.blit()
				ck=ck+1
		if y == 26:
			p=bric.Bricks(10,26,"UCL")
			p.blit()

		if y == 166:
			p=bric.Bricks(10,166,"UCL")
			p.blit()
		if y == 255:
			p=bric.Bricks(10,255,"UCL")
			p.blit()
		
	if char == "q":
		break
	if char == "p":
		pause()

	if char == "d" and main.board[x][y+1] ==  '   ':
		m.remove(x,y)
		m.sety(y+1)
		y=y+1
		m.show()
		if y > (start+end)/2:
			start=start+1
			end=end+1

	if char == "d":

		if main.board[x][y+1] == '$$$':
			os.system('aplay coin.wav&')
			score=score+10
			m.remove(x,y)
			m.sety(y+1)
			y=y+1
			m.show()

		elif main.board[x][y+1] == "PUP" or main.board[x][y+1]=="UCL":	
			if main.board[x][y+1] == 'UCL':
				size = 2
				invinsible = 1
			else:
				size = 1
				os.system('aplay power.wav&')
			m.remove(x,y)
			m.remove(x,y)
			m.sety(y+1)
			y=y+1
			m.show()

		elif main.board[x][y+1] == "(^)":
			if lives>0:
				m.remove(x,y)

	if size == 1:
		m=mario(x,y,"!O!")
	
	if size == 0:
		m=mario(x,y,"!o!")
	
	if size == 2:
    		m=mario(x,y,"!W!")
	
	if char == "a" and main.board[x][y-1] == '$$$':
		os.system('aplay coin.wav&')
		score=score+10
		m.remove(x,y)
		m.sety(y-1)
		y=y-1
		m.show()
	
	elif char == "a" and main.board[x][y-1]=='   ':
	
		if y > start:
			m.remove(x,y)
			m.sety(y-1)
			y=y-1
			m.show()
	
	elif char == "a":
		if main.board[x][y-1]=='PUP' or main.board[x][y-1]=='UCL':
			if main.board[x][y-1]=='UCL':
				size = 2
				invinsible = 1
			else:
				size = 1
				os.system('aplay power.wav&')
			m.remove(x,y)
			m.sety(y-1)
			y=y-1
			m.show()
			 

	if char == "w" and flag==0 and main.board[x-1][y] == '   ':
		os.system('aplay jump.wav&')
		flag=1
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()

	elif flag==1 and main.board[x-1][y] == '   ':
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
		flag=2

	elif flag==2 and main.board[x-1][y] == '   ':
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()
		flag=3

	elif flag==3 and main.board[x-1][y] == '   ':
		flag=4
		m.remove(x,y)
		m.setx(x=x-1)
		x=x-1
		m.show()

	elif flag==4:
	
		if main.board[x+1][y] == '___':
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
	
		if main.board[x+1][y]!='   ':
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

		if main.board[x+1][y]=='   ':
			flag=14-x
	
	elif main.board[x+1][y] == '___' and x < 14 and abgrnd == 1:
		flag = 0

	elif x==14:
		abgrnd=0
		flag=0
	
	elif flag==4 and abgrnd==1 and main.board[x+1][y]=='   ':
		abgrnd=0
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
		
		if main.board[x+1][y]=='___':
			abgrnd=0
			flag=0
	
	elif main.board[x+1][y]=='   ':
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
	
	elif main.board[x+1][y]=='(^)':
		m.remove(x,y)
		m.setx(x=x+1)
		x=x+1
		m.show()
	
	if main.board[x-1][y]=='___' and size==1 and flag!=0:
		main.board[x-1][y]='   '
	
	if main.board[x-1][y]=='$$$' and flag!=0:
		os.system('aplay coin.wav&')
		score=score+10
		main.board[x-1][y]='   '
	if enloc==6:

		for j in ben:
			if invinsible == 1:
				col2 = 1
				killedboss = 1
				invinsible_y = invinsible_y + 1
				if invinsible_y > 400:
					invinsible = 0
					invinsible_y = 0
					size = 0
			else:
				col2=collision(x,y,j.x,j.y)
				killedboss
				if size == 1:
					killedboss=killboss(x,y,j.x,j.y)
				else:
    					killedboss=0
			if col2==0 and killedboss==0:
				j.remove(j.x,j.y)
				j.sety(j.x,j.y)
				if j.life >= 0:
					j.show()
			elif col2==1 and killedboss==0:
				if size==1 and j.life >= 0:
					size=0
				else:
					if j.life >= 0:	
						lives=lives-1
						m.remove(x,y)
						if y < 122: 
							time.sleep(1)
							start=0
							end=36
							m.setx(14)
							x=14
							m.sety(0)
							y=0
						else:
							start=122
							end=158
							m.setx(14)
							x=14
							m.sety(123)
							y=123
						ck=1
				j.remove(j.x,j.y)
				j.sety(j.x,j.y)
				if j.life >= 0:
					j.show()
					col1=0
			elif killedboss==1 and col2==1:
				for j in ben:
					j.remove(j.x,j.y)
					score=score+10
					killed=0
			elif killedboss==1 and col2==0:
				for j in ben:
					if j.life < 0:
						j.remove(j.x,j.y)
				score=score+100
				killedboss=0
		
		for i in en:
			
			if invinsible == 1:
				col1 = 1
				killed = 1
				invinsible_y = invinsible_y + 1
				if invinsible_y > 400:
					invinsible = 0
					invinsible_y = 0
					size = 0
			else:
				col1=collision(x,y,i.x,i.y)
				killed
				killed=kill(x,y,i.x,i.y)
			
			if col1==0 and killed==0:
				i.remove(i.x,i.y)
				i.sety(i.x,i.y)
				if i.life == 1:
					i.show()

			elif col1==1 and killed==0:
			
				if size==1 and i.life == 1:
					size=0

				else:
					if i.life==1:	
						lives=lives-1
						os.system('aplay death.wav&')
						time.sleep(2)
						m.remove(x,y)
						if y < 122:
							start=0
							end=36
							m.setx(14)
							x=14
							m.sety(0)
							y=0
						else:
							start = 122
							end = 158
							m.setx(14)
							x=14
							m.sety(122)
							y=122
						ck=1
				i.remove(i.x,i.y)
				i.sety(i.x,i.y)
				if i.life == 1:
					i.show()
				col1=0

			elif killed==1 and col1==1:
				for i in en:
					i.remove(i.x,i.y)
					score=score+10
					killed=0
			elif killed==1 and col1==0:
				for i in en:
					if i.life == -1:
						i.remove(i.x,i.y)
				score=score+10
				killed=0
		enloc=0
	if(stair_count == 5):
		for i in st:
			i.show()
			i.remove(i.x,i.y)
			i.setx(i.x,i.y)
			i.sety(i.y)
			i.show()
			stair_count = 0
	stair_count += 1

	if(stars_count == 5):
		for i in star:
			i.show()
			i.remove(i.x,i.y)
			i.setx(i.x,i.y)
			i.sety(i.y)
			i.show()
			stars_count = 0
	stars_count += 1

	if bossen > 80 and y > 260:
		e=enemy(14,285,"(^)","*o*")
		en.append(e)
		bossen=0

	bossen=bossen+1
	
	print(y)
	print(x)
	if timer < 500 and timer > 497:
		os.system('aplay out_of_time.wav&')
	if lives<0 or timer<0:
		break
	if y >= 297 and y <=299:
		os.system('aplay explosion.wav&')
		time.sleep(1)
	if y >= 303:
		break
	time.sleep(0.070)
if y >= 302:
	os.system('aplay world_clear.wav&')

	time.sleep(2)

	print("Congratulations! You've saved the princess and won the game")
else:
    print("You lost the game!")


