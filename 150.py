from operator import *

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        mapOp = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
        }
        stack = []
        for t in tokens:
            if t in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(mapOp[t](a,b))
            else:
                stack.append(int(t))

	return stack[0]
# print (Solution().evalRPN(["2", "1", "+", "3", "*"]))
# print (Solution().evalRPN(["4", "13", "5", "/", "+"]))
# print (Solution().evalRPN(["4", "3", "-"]))
print (Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

