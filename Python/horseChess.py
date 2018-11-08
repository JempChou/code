# 使用深度优先与贪心算法解决马踏棋盘的问题

X = Y = 8
DEBUG = 0
def getOutPoints(pos, M):
	Arr = [(pos[0]+1, pos[1]+2),
	(pos[0]+1, pos[1]-2),
	(pos[0]+2, pos[1]+1),
	(pos[0]+2, pos[1]-1),
	(pos[0]-1, pos[1]+2),
	(pos[0]-1, pos[1]-2),
	(pos[0]-2, pos[1]+1),
	(pos[0]-2, pos[1]-1)]
	Arr = [(x,y) for x, y in Arr if (x>=0 and y>=0 and x<X and y<Y and M[x][y]==0)]
	return Arr

def getPriorArr(pos, M):
	Arr = getOutPoints(pos,M)
	outsNum = [len(getOutPoints(_,M)) for _ in Arr]
	return [x for _,x in sorted(zip(outsNum, Arr))]

def fun(pos, M, step):
	ret = False
	M[pos[0]][pos[1]] = step
	if DEBUG: print(pos,step,M)
	if step == X*Y :
		print(M)
		return True
	Arr = getPriorArr(pos,M)
	if len(Arr) == 0:
		return False
	step += 1
	for ele in Arr:
		ret = fun(ele,M,step)
		if ret == True:
			break
	return ret

import numpy as np
def main():
	pos = (0,0)
	M = np.zeros((X,Y))
	# M = [[0 for _ in range(X)] for i in range(Y)]

	step = 1
	ret = fun(pos,M,step)
	print(ret)


if __name__ == '__main__':
	main()
