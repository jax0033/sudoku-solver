import os
import pygame
import numpy as np
import time

global timer_d0c
timer_d0c = 0

"""
import requests
used to download a random sudoku from sudoku.com and solve it
"""

#sets window location to 400,75 (changes environmental "variable SDL_VIDEO_WINDOW_POS")
os.environ['SDL_VIDEO_WINDOW_POS'] = "400,75"

pygame.init()
screen = pygame.display.set_mode((900,900))
width,heigth = 900,900

font = pygame.font.SysFont(None,60)

#2dimensional array
grid = [[5,1,2,4,0,9,0,6,3],
		[0,6,0,0,2,3,0,9,4],
		[0,3,9,5,6,0,8,1,2],
		[2,7,0,9,0,0,0,3,1],
		[9,0,0,0,1,0,0,8,7],
		[3,8,0,0,4,6,2,5,9],
		[0,0,0,0,0,4,0,7,8],
		[0,2,8,6,9,0,3,4,0],
		[0,4,0,0,7,5,9,2,6]]


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

#returns all possible numbers at (x,y)
def possible_nums(x,y):
	possible = []
	if grid[y][x] == 0:
		ongrid = allnums(x,y)
		lst = [i for i in range(1,10)]
		for el in lst:
			if el not in ongrid:
				possible.append(el)
		print(possible)
		if len(possible) == 0:
			return False
		return possible
	return False

#solves the grid using backtracking and recursion
#this is, by far, the worst mess i have encountered yet. It does work..
def solve(sgrid,temp):
	global temp3
	for x in range(9):
		for y in range(9):
			if sgrid[y][x] == 0:
				for n in range(1,10):
					if is_possible(x,y,n):
						temp3 = temp
						sgrid[y][x] = n
						solve(sgrid,temp)
						sgrid[y][x] = 0
				#if the program cant recurse anymore it means the sudoku is finished
				return
	temp3.append(np.matrix(sgrid))


#solve(grid)



def solve_anim(sgrid):
	global timer_d0c
	screen.fill((255,255,255))
	for x in range(9):
		for y in range(9):
			if sgrid[y][x] == 0:
				for n in range(1,10):
					if is_possible(x,y,n):
						sgrid[y][x] = n
						mod_draw_board(np.matrix(sgrid))
						solve_anim(sgrid)
						sgrid[y][x] = 0
				mod_draw_board(np.matrix(sgrid))
				return
	input("Different one?")




def drawgrid():
	for n in range(1,3):
		pygame.draw.line(screen,(0,0,0),(n*(width/3),0),(n*(width/3),heigth),5)
		pygame.draw.line(screen,(0,0,0),(0,n*(heigth/3)),(width,n*(heigth/3)),5)
	for n in range(1,10):
		pygame.draw.line(screen,(0,0,0),(n*(width/9),0),(n*(width/9),heigth),1)
		pygame.draw.line(screen,(0,0,0),(0,n*(heigth/9)),(width,n*(heigth/9)),1)

def drawboard(board,font):
	for x in range(9):
		for y in range(9):
			if board[y][x] != 0:
				draw_text(board[y][x],font,x,y)

def mod_draw_board(board):
	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
	screen.fill((255,255,255))
	drawgrid()
	print(board)
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
				#time.sleep()
			c+=1
	pygame.display.update()





def bigtile(x,y):
	pygame.draw.rect(screen,(255,0,0),(x,y,299,299),3)

def smalltile(rect):
	pygame.draw.rect(screen,(255,0,0),rect,3)

def draw_text(text,font,x,y):
	text = str(text)
	textobj = font.render(text,1,(0,0,0))
	screen.blit(textobj,pygame.Rect(x*100+30,y*100+30,100,100))


def main():
	global temp3
	font = pygame.font.SysFont(None,60)
	pygame.display.set_caption("Sudoku")
	
	n = 0
	rectangles = []
	used_tiles = []
	board = []
	temp_b09 = []
	
	solve(grid,[])
	temp3 = str(temp3[0])
	
	for s in temp3:
		if s.isdigit():
			temp_b09.append(int(s))
	
	#constructing necessary board/controls
	for y in range(9):
		for x in range(9):
			rectangles.append([pygame.Rect(x*100,y*100,100,100),(x,y),False,None],)

			if grid[y][x] != 0:
				rectangles[n] = [pygame.Rect(x*100,y*100,100,100),(x,y),True,grid[y][x]]
				board.append([grid[y][x],(x,y),True])
				used_tiles.append((x,y))
			n+=1

	initialize_skynet_algorithm = False
	selection = False
	key = None
	selector = None
	fps = 30
	clock = pygame.time.Clock()
	having_fun_solving_the_sudoku = True
	while having_fun_solving_the_sudoku:

		if initialize_skynet_algorithm:
			solve_anim(grid)
			l = 0
			for x in range(9):
				for y in range(9):
					draw_text(temp_b09[l],font,y,x)
					pygame.display.update()

					l += 1
			time.sleep(20)
			having_fun_solving_the_sudoku = False
		else:
			click = False
			key = None
			screen.fill((255,255,255))
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

					if event.key == pygame.K_SPACE:
						initialize_skynet_algorithm = True

			for rect in rectangles:
				if rect[0].collidepoint((mx,my)):
					if click:
						selector = rect
						selection = True

			if selection:
				smalltile(selector[0])
				temp = True
				for tile in rectangles:
					if selector[1] == tile[1] and tile[2] is not True and key is not None:
						for n,all_ in enumerate(rectangles):
							if all_[1] == selector[1]:
								rectangles[n][-1] = key
								key = None


			ugrid = []
			for tile in rectangles:
				if tile[-1] == None:
					ugrid.append(0)
				else:
					ugrid.append(tile[-1])
				if tile[-1] != None:
					draw_text(tile[-1],font,tile[1][0],tile[1][1])
			if temp_b09 == ugrid:
				having_fun_solving_the_sudoku = False

		clock.tick(fps)
		pygame.display.update()

main()
print("finished")
