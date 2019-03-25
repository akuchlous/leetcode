import pdb
class Solution:
    def decodeString(self, s):
        stack = []
        i, l , buf = 0, len(s), ""
        while (i < l):
            if (s[i] == "["):
                stack.append(buf) 
                stack.append("[") 
                buf = ""
            elif (s[i] == "]"):
	        pdb.set_trace()
                # pop 1 and multiple 
                ele = stack.pop()
		pushV = ele
		while (ele != "["):
		    if (ele.isdigit()): 
		        pushV *=int(ele)
		    else:
		        pushV = pushV + ele 
                stack.append(pushV)
            else:
	        if (s[i].isdigit() and buf!=""):
		    stack.append(buf)
		    buf=s[i]
		else:
                    buf+=s[i]
            i+=1 
        
        return ("".join(stack))


print (Solution().decodeString("3[a2[c]]"))
