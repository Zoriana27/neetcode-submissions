class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            curr_min = self.stack[-1][0]
            curr_min = min(curr_min, val)
        else:
            curr_min = val
        self.stack.append([curr_min, val])
        

    def pop(self) -> None:
        curr_min, val = self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]
        
