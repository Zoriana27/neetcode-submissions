class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if c in mapping: #if c is a closing bracket
                if not stack or stack[-1] != mapping[c]:
                    #if the stack is empty or the top element in the stack isn't the corresponding opening bracket
                    return False
                stack.pop() #if it is a corresponding opening bracket, pop it
            else:
                stack.append(c) #if c is an open bracket
        if stack:
            return False
        else:
            return True