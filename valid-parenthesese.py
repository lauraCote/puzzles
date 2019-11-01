class Solution:
    def isValid(self, parentheses: str) -> bool:
        parenthesesMatch = { '(': ')', '{': '}', '[': ']'}
        parenthesesStack = []
        for parenthese in parentheses:
            if parenthesesMatch.get(parenthese) != None:
                parenthesesStack.append(parenthese)
            else:
                if len(parenthesesStack) <= 0:
                    return False
                if parenthesesMatch.get(parenthesesStack[-1]) != parenthese:
                    return False
                parenthesesStack.pop()
        return len(parenthesesStack) == 0 

print(Solution().isValid(""))
                
                    
            
