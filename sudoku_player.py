import os
import pygame
import numpy as np
import time
import random
import getsudoku as sk

global timer_d0c
global temp3

temp3 = []
timer_d0c = 0

#sets window location to 400,75 (changes environmental "variable SDL_VIDEO_WINDOW_POS")
os.environ['SDL_VIDEO_WINDOW_POS'] = "400,75"

pygame.init()
screen = pygame.display.set_mode((900,900))
width,heigth = 900,900
background  = pygame.image.load("background.png")
font = pygame.font.SysFont(None,60)

#2dimensional array
"""
grid = [[5,1,2,4,0,9,0,6,3],
		[0,6,0,0,2,3,0,9,4],
		[0,3,9,5,6,0,8,1,2],
		[2,7,0,9,0,0,0,3,1],
		[9,0,0,0,1,0,0,8,7],
		[3,8,0,0,4,6,2,5,9],
		[0,0,0,0,0,4,0,7,8],
		[0,2,8,6,9,0,3,4,0],
		[0,4,0,0,7,5,9,2,6]]

"""
grid = sk.getsudoku()

#detects the square of (x,y) and set their values to the square origin
def square(x,y):
	if x in [0,1,2]:
		setx = 0
	elif x in [3,4,5]:
		setx = 3
	elif x in [6,7,8]:
		setx = 6
	
	if y in [0,1,2]:
		sety = 0
	elif y in [3,4,5]:
		sety = 3
	elif y in [6,7,8]:
		sety = 6
	y,x = sety,setx
	squaren = []
	for n in range(3):
		x = setx
		for m in range(3):
			squaren.append(grid[y][x])
			x+=1
		y+=1
	squaren = list(set(squaren))
	return squaren

#all numbers on the x y axis
def cross(x,y):
	all_nums = []
	for n in range(9):
		all_nums.append(grid[n][x])
		all_nums.append(grid[y][n])
	all_nums = list(set(all_nums))
	return all_nums

#all numbers in the same square, x and y axis as (x,y)
def allnums(x,y):
	allnums = []
	squares = square(x,y)
	crosss = cross(x,y)
	for n in squares:
		allnums.append(n)
	for n in crosss:
		allnums.append(n)
	allnums = list(set(allnums))
	return allnums

#checks if it is possible to put a number at (x,y)
def is_possible(x,y,num):
	if grid[y][x] == 0:
		ongrid = allnums(x,y)
		if num not in ongrid:
			return True
	return False

#solves the grid using backtracking and recursion
def solve(sgrid):
	global temp3
	for x in range(9):
		for y in range(9):
			if sgrid[y][x] == 0:
				for n in range(1,10):
					if is_possible(x,y,n):
						sgrid[y][x] = n
						solve(sgrid)
						sgrid[y][x] = 0
				#if the program cant recurse anymore it means the sudoku is finished
				return
	temp3.append(np.matrix(sgrid))

#converts temp3 into lists with solutions
solutions = []
solve(grid)
temp4 = ""
for s in temp3:
	temp4 += str(s) + " "
temp3 = temp4.split("] [")
for n,j in enumerate(temp3):
	j = str(j)
	solutions.append([])
	for c in j:
		if c.isdigit():
			solutions[n].append(int(c))

def solve_anim(sgrid):
	for y in range(9):
		for x in range(9):
			if sgrid[y][x] == 0:
				for n in range(1,10):
					if is_possible(x,y,n):
						screen.blit(background,(0,0))
						drawgrid()
						sgrid[y][x] = n
						#mod_draw_board(np.matrix(sgrid))
						smalltile(pygame.Rect(x*100,y*100,100,100),color=(0,255,0),size=5)
						#pygame.display.update()
						mod_draw_board(np.matrix(sgrid))
						solve_anim(sgrid)
						screen.blit(background,(0,0))
						drawgrid()
						sgrid[y][x] = 0
						smalltile(pygame.Rect(x*100,y*100,100,100),color=(255,0,0),size=5)
						mod_draw_board(np.matrix(sgrid))
						#pygame.display.update()
				return
	mod_draw_board(np.matrix(sgrid),True)
	input("Different one?")

def drawgrid():
	for n in range(1,3):
		pygame.draw.line(screen,(0,0,0),(n*(width/3),0),(n*(width/3),heigth),5)
		pygame.draw.line(screen,(0,0,0),(0,n*(heigth/3)),(width,n*(heigth/3)),5)
	for n in range(1,10):
		pygame.draw.line(screen,(0,0,0),(n*(width/9),0),(n*(width/9),heigth),1)
		pygame.draw.line(screen,(0,0,0),(0,n*(heigth/9)),(width,n*(heigth/9)),1)

def mod_draw_board(board,oo=False):
	if oo:
		screen.blit(background,(0,0))
		drawgrid()
	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
	temp_47e = []
	board = str(board)

	for s in board:
		if s.isdigit():
			temp_47e.append(int(s))
	c = 0
	for x in range(9):
		for y in range(9):
			if temp_47e[c] != 0:
				draw_text(temp_47e[c],font,y,x)
				time.sleep(0.0015)
			c+=1
	pygame.display.update()

def smalltile(rect,color=(255,0,0),size=3):
	pygame.draw.rect(screen,color,rect,size)

def draw_text(text,font,x,y):
	text = str(text)
	textobj = font.render(text,1,(0,0,0))
	screen.blit(textobj,pygame.Rect(x*100+33,y*100+28,100,100))

def draw_text_selection(text,x,y):
	text = str(text)
	font = pygame.font.SysFont(None,30)
	textobj = font.render(text,1,(130,130,130))
	screen.blit(textobj,pygame.Rect(x*100+10,y*100+10,100,100))

def main():
	
	#temp3 stores the finished sudoku
	global temp3
	global solved__
	font = pygame.font.SysFont(None,60)
	pygame.display.set_caption("Sudoku")
	
	#contains information about [<Rect> obj, position, mutability, displayed number]
	rectangles = []

	#all tile information (hitbox,pos,immutability,number)
	n = 0
	for y in range(9):
		for x in range(9):
			rectangles.append([pygame.Rect(x*100,y*100,100,100),(x,y),False,None])

			if grid[y][x] != 0:
				rectangles[n] = [pygame.Rect(x*100,y*100,100,100),(x,y),True,grid[y][x]]
			n+=1

	#bools for controlling loops and selections
	solve_sudoku = False
	selection = False
	solved__ = False
	running = True

	selector = None
	clock = pygame.time.Clock()
	fps = 30
	while running:

		if solve_sudoku:
			solved__ = True
			solve_anim(grid)
			l = 0
			screen.blit(background,(0,0))
			for x in range(9):
				for y in range(9):
					drawgrid()
					draw_text(solutions[-1][l],font,y,x)
					l += 1
			pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,0,900,900),3)
			pygame.display.update()
			running = False

		else:

			click = False
			key = None
			screen.blit(background,(0,0))
			drawgrid()

			mx,my = pygame.mouse.get_pos()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						click = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						key = 1
					if event.key == pygame.K_2:
						key = 2
					if event.key == pygame.K_3:
						key = 3
					if event.key == pygame.K_4:
						key = 4
					if event.key == pygame.K_5:
						key = 5
					if event.key == pygame.K_6:
						key = 6
					if event.key == pygame.K_7:
						key = 7
					if event.key == pygame.K_8:
						key = 8
					if event.key == pygame.K_9:
						key = 9
					if event.key == pygame.K_0:
						key = 10
					if event.key == pygame.K_SPACE:
						solve_sudoku = True

			for rect in rectangles:
				if rect[0].collidepoint((mx,my)):
					if click:
						selector = rect
						selection = True

			#if a tile is selected:
			if selection:
				#visually displays what tile is selected
				smalltile(selector[0],(100,0,255))
				for tile in rectangles:
					if selector[1] == tile[1] and tile[2] is not True and key is not None:
						for n,all_ in enumerate(rectangles):
							if all_[1] == selector[1]:
								if key != 10:
									rectangles[n][-1] = key
									key = None
								else:
									rectangles[n][-1] = None
									key = None

			#clears ugrid
			ugrid = []

			for tile in rectangles:
				if tile[-1] == None:
					ugrid.append(0)
				else:
					ugrid.append(tile[-1])
				if tile[-1] != None:
					if tile[-2] == False:
						draw_text_selection(tile[-1],tile[1][0],tile[1][1])
					else:
						draw_text(tile[-1],font,tile[1][0],tile[1][1])
			for solution in solutions:
				if solution == ugrid:
					pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,0,900,900),3)
					running = False

		clock.tick(fps)
		pygame.display.update()

main()
if solved__ == True:
	print("All possible solutions have been displayed.")
else:
	print("Congratulations, you did it!")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()
