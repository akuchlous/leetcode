class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mapS = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9 }
        N1 = 0
        i = 0
        for n in reversed(num1):
            N1 += mapS[n]*pow(10,i)
            i+=1
        i = 0
        N2 = 0 
        for n in reversed(num2):
            N2 += mapS[n]*pow(10,i)
            i+=1
        p = N2 * N1 
        print (N1 , "*",  N2)
        print(p)
        ret = ""
        mapR = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9" }
        while (p > 0):
            ret = mapR[p%10]+ret
            p = p//10
        return ret


print (Solution().multiply("6913259244", "491555843274052722"))
