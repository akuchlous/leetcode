import json
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

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
                Arr[p.x+abs(minC)][p.y+abs(minC)] = [1,[1,1,1,1]]
                    
	# for r in range(0,maxC):
	# 	print (Arr[r])
	max = 0
	for i in range(0,maxC):
		for j in range(0,maxC):
			if (Arr[i][j][0] == 1):
				# check left
				# if (((j-1) > 0) and Arr[i][j-1][0] == 1):
				if (j-1 >= 0) :
					Arr[i][j][1][0]+= Arr[i][j-1][1][0]
				# check top
				# if (((i-1) > 0) and Arr[i-1][j][0] == 1):
				if (i-1 >= 0) :
					Arr[i][j][1][1]+= Arr[i-1][j][1][1]
				# check left diag
				# if ((((i-1) > 0) and (j-1)>0) and Arr[i-1][j-1][0] == 1):
				if (i-1 >= 0):
					Arr[i][j][1][2]+= Arr[i-1][j-1][1][2]
				# check right diag
				# if ((((i-1) > 0) and (j+1)<maxC) and Arr[i-1][j+1][0] == 1):
				if (i-1 >= 0 and j+1<maxC) :
					Arr[i][j][1][3]+= Arr[i-1][j+1][1][3]
	maxN = 0
	for r in range(0,maxC):
		for c in range(0,maxC):
			for v in range(0,4):
		 		if (maxN < Arr[r][c][1][v]):
		 			maxN = Arr[r][c][1][v]
	return maxN

def stringToPoint(input):
    tokens = json.loads(input)
    return Point(tokens[0], tokens[1])

def stringToPointArray(pointArrays):
    points = []
    for pointArray in pointArrays:
        points.append(stringToPoint(json.dumps(pointArray)))
    return points

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    # while True:
    #     try:
    #         line = lines.next()
    l = [[1,1],[2,2],[3,3]]

    points = stringToPointArray(l)
    ret = Solution().maxPoints(points)
    out = intToString(ret)
    print out

if __name__ == '__main__':
    main()
