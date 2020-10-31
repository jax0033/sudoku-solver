import requests


def getsudoku():
	url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&?level=3"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
	result = requests.get(url, headers=headers).content.decode()
	grid = [[0 for i in range(9)] for i in range(9)]
	result = result.split("squares")
	result = str(result[1])
	res = ""
	for char in result:
		if char.isdigit():
			res += char
	x = [int(res[i*3]) for i in range(len(res)//3)]
	y = [int(res[i*3+1]) for i in range(len(res)//3)]
	val = [int(res[i*3+2]) for i in range(len(res)//3)]
	for n in range(len(val)):
		grid[y[n]][x[n]] = val[n]
	return grid


#string to grid
def format(strg):
	grid = []
	row = []
	for n in range(9):
		for i in range(9):
			row.append(int(strg[n*9+i]))
		grid.append(row)
		row = []
	return grid

#grid to string
def formatstr(grid):
	ret = ""
	grid = str(grid)
	for char in grid:
		print(char)
		if char.isdigit() == True:
			ret += char
	return char



