import numpy as np

"""
import requests
used to download a random sudoku from sudoku.com and solve it
"""
#2dimensional array
grid = [[5,1,2,4,0,9,0,6,3],
		[0,6,0,0,2,3,0,9,4],
		[0,3,9,5,6,0,8,1,2],
		[2,7,0,9,0,0,0,3,1],
		[9,0,0,0,1,0,0,8,7],
		[3,8,0,0,4,6,2,5,9],
		[0,0,0,0,0,4,0,7,8],
		[0,2,8,6,9,0,3,4,0],
		[0,4,0,0,7,5,9,2,6]	]


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
	#goes through the square and appends all values to squaren
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
def solve(sgrid):
	for x in range(9):
		for y in range(9):
			if sgrid[y][x] == 0:
				for n in range(1,10):
					if is_possible(x,y,n):
						sgrid[y][x] = n
						solve(sgrid)
						sgrid[y][x] = 0
				return
	#ürints the result(s) in a readable format
	print(np.matrix(sgrid))

solve(grid)
