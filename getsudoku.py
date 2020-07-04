import requests

def getsudoku():
	url = "https://grid.websudoku.com/"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
	result = requests.get(url, headers=headers).content.decode()

	result = result.split('"')
	temp_0dc = []
	for e in result:
		if e.isdigit() and len(e) == 81:
			temp_0dc.append(e)

	grid = [[0 for i in range(9)] for i in range(9)]
	k = 0
	for x in range(9):
		for y in range(9):
			if temp_0dc[1][k] == "1":

				grid[x][y] = int(temp_0dc[0][k])
			else:
				grid[x][y] = 0
			k+=1
	 
	return grid
