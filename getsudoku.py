import requests

def getsudoku():
	url = "https://grid.websudoku.com/"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
	result = requests.get(url, headers=headers).content.decode()

	result = result.split("SIZE=2 AUTOCOMPLETE=off NAME=")
	temp = ""
	for s in result:
		temp += s + ""
	temp = temp.split(" ")

	temp_0dc = []
	for n,s in enumerate(temp):
		if s.upper().startswith("MAXLENGTH") or s.upper().startswith("READONLY"):
			temp_0dc.append([temp[n],temp[n+1]])

	grid = [[0 for i in range(9)] for i in range(9)]
	k = 0
	for x in range(9):
		for y in range(9):
			if temp_0dc[k][0].upper() == "READONLY":
				grid[x][y] = int(temp_0dc[k][1][-2])
			else:
				grid[x][y] = 0
			k+=1
	 
	return grid
