class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["*", "/", "-", "+"]
        
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                arg1 = stack.pop()
                arg2 = stack.pop()
                if tokens[i] == "*":
                    stack.append(arg2 * arg1)
                elif tokens[i] == "/":
                    stack.append(int(arg2 / arg1))
                elif tokens[i] == "-":
                    stack.append(arg2 - arg1)
                else:
                    stack.append(arg2 + arg1)
        
        return stack[0]