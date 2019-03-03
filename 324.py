import pdb
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def recurse (s):
	    pdb.set_trace()
	    if (s[0] == "["): s= s[1:]
            for i in range(len(s)):
                if (s[i] == "]" or s[i] == ","):
                    if (s[i] == "]"): 
                        N = NestedInteger([int(s[:i])])
                    else:
                        N = NestedInteger([int(s[:i]), recurse(s[i:])])
            return N
        
        if s == ""  : return None
        return recurse(s)


print (Solution().deserialize("324"))
