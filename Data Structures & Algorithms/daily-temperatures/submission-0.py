class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = i - j
            
            stack.append(i)

        while len(stack) > 0:
            output[stack.pop()] = 0
        
        return output
            


