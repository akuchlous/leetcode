import pdb
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        blockC = False
        newList = []
	pdb.set_trace()
        for line in source:
            # is in block
            if (blockC) :
                if ("*/" not in line  ): continue
                i = line.find("*/")
                line = line[i:]
                blockC = False
                 
            if ("/*" in line):
                i = line.find("/*")
                if (line[:i] !="") : newList.append(line[:i])
                blockC = True
            elif ("//" in line):
                i = line.find("//")
                if (line[:i] !="") : newList.append(line[:i])
            else:
                newList.append(line)
            
        return newList

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print (Solution().removeComments(source))
