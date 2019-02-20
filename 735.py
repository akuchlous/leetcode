import pdb
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        aliveA = []
        pdb.set_trace()
        for a in asteroids:
            if ((a > 0) or (len(aliveA) == 0)):
                aliveA.append(a)
            else:
                while (True):
                    if (len(aliveA) == 0):
                        aliveA.append(a)
                        break
                    elif (aliveA[-1] > 0):
                        if (aliveA[-1] > abs(a)):
                            break
                        elif (aliveA[-1] == abs(a)):
                            aliveA.pop()
                            break
                        else:
                            aliveA.pop()
                    else:
                        aliveA.append(a)
                        break

        return aliveA

#print (Solution().asteroidCollision([-2,-1,1,2]))
print (Solution().asteroidCollision([1,-2,-2,-2]))
