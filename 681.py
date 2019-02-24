import pdb
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        def newTime(time, replaceChar):
            modTime = time.replace(":","")
            minT = min(modTime)
            # "A" > "0"
            pos = len(modTime)
            for c in modTime[::-1]:
                nextTime = "A"
                pos-=1
                for n in replaceChar:
                    if (n>c):
                        if (pos == 2 and n > "5"): continue
                        if (pos == 0 and n > "2"): continue
                        nextTime = min(nextTime, n)
                if (nextTime != "A"):
                    break
            if (pos == -1): return time
	    
            retVal =  modTime[:pos] + nextTime + minT*(len(modTime)-1-pos )
	    return retVal

        charList = time[::-1].replace(":","")
	minC = min(charList)
        retVal = newTime(time, charList)
	if (retVal == time) or (retVal[:2] > "24"):
            retVal =  minC+minC+minC+minC

        return retVal[:2]+":"+retVal[2:]

##print (Solution().nextClosestTime("00:00"))
print (Solution().nextClosestTime("13:40"))
print (Solution().nextClosestTime("23:59"))
