
class Solution:
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		intervals = sorted(intervals, key=lambda x: x[0])
		unmerge = []
		for  i in range(0, len(intervals)-1):
			if (intervals[i][1] >= intervals[i+1][0]):
				intervals[i+1][0] = intervals[i][0]
				intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
			else:
				unmerge.append(intervals[i])
		unmerge.append(intervals[len(intervals)-1])
		
		return unmerge


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

