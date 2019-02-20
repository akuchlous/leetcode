import pdb
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(" ")
        if (str == ""): return 0
        neg = 1
        # if (debug):
        #       pdb.set_trace()
        while True:
                if (str == ""): return 0
                if (str[0] == "-" or str[0] == "+"):
                        neg *= int(str[0]+"1")
                        str = str[1:]
                        break
                else:
                        break
        if (str == "") : return 0
        if (str[0]<"0" or str[0]>"9"):
            return 0
        index = 0
        for i in range(0,len(str)):
            if (str[i]<"0" or str[i]>"9"):
                break
            index +=1
        val = int(str[:index])
        if (2147483648 <= val):
                if (neg == -1):
                    return -2147483648
                else:
                    return 2147483647
        val*= neg
        return val

s = Solution()
print s.myAtoi("12121")
print s.myAtoi("-12121")
print s.myAtoi("+12121")
print s.myAtoi(" +12121")
print s.myAtoi(" -12121")
print s.myAtoi("v -12121")
print s.myAtoi("v12121")
print s.myAtoi("12b121")
print s.myAtoi("work 2")
print s.myAtoi("wo k 2")
print s.myAtoi("")
print s.myAtoi("+")
print s.myAtoi("-")
print s.myAtoi("---")
print s.myAtoi("+ ")
print s.myAtoi(" ")
print s.myAtoi("-91283472332")
print s.myAtoi("-+2")
print s.myAtoi("--2")
print s.myAtoi("+-2")
