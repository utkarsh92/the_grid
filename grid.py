import pip

package = 'termcolor'
try:
    __import__(package)
except ImportError:
    pip.main(['install', package])

#MAIN CODE
from termcolor import colored, cprint
import random as rand
from time import sleep
import os

c = 19
r = 11
grid = [[0 for _ in range(c)] for _ in range(r)]

#dot
vel = (0,0)
dotC = -1
dotR = -1
dType = 1

def randomGrid():
	global grid
	for i in range(r):
		for j in range(c):
			grid[i][j] = rand.choice([0,1])

def flipSign(s):
	return s*-1

def moveDot():
	global vel,dotC,dotR,grid,dType
	if vel == (0,0):
		#first time
		dotC = randC = rand.randrange(0,c,1)
		dotR = randR = rand.randrange(0,r,1)
		try:
			grid[dotR][dotC] = 1
		except:
			print("err1:")
			print("dotR",dotR)
			print("dotC",dotC)
			print("vel",vel, "\n")
			exit()

		v1 = rand.choice([1,-1])
		v2 = rand.choice([1,-1])
		vel = (v1,v2)

		# print("first:")

	# print("dotR",dotR)
	# print("dotC",dotC)
	# print("vel",vel, "\n")

	#velocity update
	if (dotR, dotC) in [(0,0),(0,c-1),(r-1,0),(r-1,c-1)]:
		#corners
		vel = (flipSign(vel[0]),flipSign(vel[1]))
	elif dotR in [0,r-1]:
		#top down wall
		vel = (flipSign(vel[0]),vel[1])
	elif dotC in [0,c-1]:
		#left right wall
		vel = (vel[0],flipSign(vel[1]))

	if vel != (0,0):
		if dType == 1:
			grid[dotR][dotC] = 0
		elif dType == 2:
			grid[dotR][dotC] = 2
		elif dType == 3:
			grid[dotR][dotC] += 1
		else:
			print("invalid dType")
			exit()
		dotR += vel[0]
		dotC += vel[1]
		try:
			grid[dotR][dotC] = 1
		except:
			print("err2:")
			print("dotR",dotR)
			print("dotC",dotC)
			print("vel",vel, "\n")
			exit()

	# print("*dotR",dotR)
	# print("*dotC",dotC)
	# print("*vel",vel, "\n")



def printCell(x,y,blank = True):
	clr = None
	bg = None
	if not blank:
		if grid[x][y] == 1:
			clr = "red"
			bg = "on_red"
		elif grid[x][y] == 2:
			clr = "yellow"
			bg = "on_yellow"
		elif grid[x][y] == 3:
			clr = "cyan"
			bg = "on_cyan"
	cprint("   ", clr, bg, end = "")
	return


def printGrid(blank = True):
	for x in range(r):
		for i in range(c):
			if i == c-1:
				print("---+", end = "\n")
			elif i != 0:
				print("---+", end = "")
			else:
				print("+---+", end = "")

		for y in range(c):
			if y == c-1:
				printCell(x,y,blank)
				print("|", end = "\n")
			elif y != 0:
				printCell(x,y,blank)
				print("|", end = "")
			else:
				print("|", end = "")
				printCell(x,y,blank)
				print("|", end = "")
	for i in range(c):
			if i == c-1:
				print("---+", end = "\n")
			elif i != 0:
				print("---+", end = "")
			else:
				print("+---+", end = "")

if __name__ == '__main__':
	size = os.get_terminal_size()
	r = (size.lines)//2 - 1
	c = (size.columns)//4 - 1
	grid = [[0 for _ in range(c)] for _ in range(r)]

	# print("r",r)
	# print("c",c,"\n\n")

	# moveDot()
	# moveDot()
	# moveDot()

	for i in range(100):
		os.system('clear')
		# randomGrid()
		moveDot()
		printGrid(False)
		sleep(0.1)





