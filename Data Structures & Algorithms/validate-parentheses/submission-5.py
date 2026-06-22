class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "{" : "}",
            "[" : "]"
        }

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            elif len(stack) != 0 and brackets[stack.pop()] == s[i]: 
                continue
            else:
                return False
        
        return len(stack) == 0

