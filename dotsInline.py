import pdb
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
	# fill in matrix
	# initialize
        maxC = 0  # Columns
        minC = 0
	for p in points:
		if (p.x> maxC): maxC = p.x
		if (p.y> maxC): maxC = p.y
                if (p.x< minC): minC = p.x
		if (p.y< minC): minC = p.y
	maxC+=abs(minC)+1
	Arr = []
        Arr = []
        for r in range(0,maxC):
                Arr.append([])
                for c in range(0, maxC):
                        Arr[r].append([0,[0,0,0,0]])

        for p in points:
                Arr[p.x+abs(minC)][p.y+abs(minC)][0] =  1
                Arr[p.x+abs(minC)][p.y+abs(minC)][1][0] += 1
                Arr[p.x+abs(minC)][p.y+abs(minC)][1][1] += 1
                Arr[p.x+abs(minC)][p.y+abs(minC)][1][2] += 1
                Arr[p.x+abs(minC)][p.y+abs(minC)][1][3] += 1
                    
	for r in range(0,maxC):
		print (Arr[r])
	pdb.set_trace()
	max = 0
	for i in range(0,maxC):
		for j in range(0,maxC):
			if (Arr[i][j][0] == 1):
				if (j-1 >= 0) :
					Arr[i][j][1][0] += Arr[i][j-1][1][0]
				if (i-1 >= 0) :
					Arr[i][j][1][1] += Arr[i-1][j][1][1]
				if (i-1 >= 0):
					Arr[i][j][1][2] += Arr[i-1][j-1][1][2]
				if (i-1 >= 0 and j+1<maxC) :
					Arr[i][j][1][3] += Arr[i-1][j+1][1][3]
			else:
				if (j-1 >= 0) :
					Arr[i][j][1][0] = Arr[i][j-1][1][0]
				if (i-1 >= 0) :
					Arr[i][j][1][1] = Arr[i-1][j][1][1]
				if (i-1 >= 0):
					Arr[i][j][1][2] = Arr[i-1][j-1][1][2]
				if (i-1 >= 0 and j+1<maxC) :
					Arr[i][j][1][3] = Arr[i-1][j+1][1][3]
	maxN = 0
	for r in range(0,maxC):
		for c in range(0,maxC):
			for v in range(0,4):
		 		if (maxN < Arr[r][c][1][v]):
		 			maxN = Arr[r][c][1][v]
                                        
        return maxN



class P(object):
	def __init__(self, x,y):
		self.x = x
		self.y = y


# print 3 ==  Solution().maxPoints([P(0,0), P(-1,-1), P(2,2)])
print 3 ==  Solution().maxPoints([P(1,1), P(1,1), P(2,3)])
