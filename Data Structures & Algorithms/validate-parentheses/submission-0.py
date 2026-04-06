class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenDict = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        for c in s:
            if c in parenDict:
                if stack and stack[-1] == parenDict[c]:
                    stack.pop()
                else:
                    return False
            else:        
                stack.append(c)
        return True if not stack else False

        