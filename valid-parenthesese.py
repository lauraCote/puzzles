class Solution:
    def isValid(self, parentheses: str) -> bool:
        parenthesesMatch = { '(': ')', '{': '}', '[':']'}
        parenthesesStack = []
        for parenthese in parentheses:
            if parenthesesMatch[parenthese] is not None:
                parenthesesStack.append(parenthese)
            else:
                if parenthesesStack.count <= 0:
                    return False
                if parenthesesMatch[parenthesesStack.pop] != parenthese:
                    return False
                parenthesesStack.remove(parenthesesStack.pop)
        return parenthesesStack.count == 0 

print(Solution().isValid("[{()}]"))
                
                    
            
