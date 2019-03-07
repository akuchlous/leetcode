class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y if x * y >= 0 else int(math.ceil(x / y)),
        }
        for s in tokens:
            if s in operators:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(operators[s](op1, op2))
            else:
                stack.append(int(s))
        return stack.pop()
        
