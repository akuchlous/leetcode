from collections import defaultdict, deque

# cycle detection
import pdb
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        depGraph = defaultdict(list)
        for edge in prerequisites:
            depGraph[edge[0]].append(edge[1])
        #pdb.set_trace()
        course = numCourses - 1 
        while (course>0):
            visited = [course]
            path = deque()
            path.append(course)
            while (len(path)>0):
                for dep in depGraph[course]:
                    if dep in visited: return False
                    path.append(dep)
                course = path.popleft()
            course -=1 
        return True
    
print(Solution().canFinish(2, [[1,0],[0,1]]))
