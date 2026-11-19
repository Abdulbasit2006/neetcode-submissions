class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {")": "(","]":"[", "}":"{"}
        for c in s:
            if c not in closetoOpen:
                stack.append(c) # apend only if c is an opening bracket
            else:
                if stack and closetoOpen[c] == stack[-1]:
                    stack.pop()
                else:
                   return False
        return len(stack) == 0


                
                

    
            
        