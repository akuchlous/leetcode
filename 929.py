import pdb
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqE = set()
        for e in emails:
            buf = ""
            foundPlus = False 
            foundAt = False 
            pdb.set_trace()
            for s in e:
                if (not foundPlus):
                    if (s == "+"):  
                        foundPlus = True
                        continue
                    elif (s =="." ): 
                        continue
                    else:
                        buf+=s
                else:
                    if (foundAt == True or s == "@"):
                        foundAt = True
                        buf+=s

            uniqE.add(buf)
        return list(uniqE)



print (Solution().numUniqueEmails(["a.bc+d@leetcode.com","a.b.c+f.g@leetcode.com","abc+david@lee.tcode.com"]))
