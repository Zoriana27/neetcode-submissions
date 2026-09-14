class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def helper(i, coordX, coordY):
            if i == len(word):
                return True
            
            if (coordX < 0 or coordX >= rows) or (coordY < 0 or coordY >= cols) or board[coordX][coordY] != word[i] or (coordX, coordY) in visited:
                return False
            visited.add((coordX, coordY))
            res = helper(i + 1, coordX + 1, coordY) or helper(i + 1, coordX - 1, coordY) or helper(i + 1, coordX, coordY + 1) or helper(i + 1, coordX, coordY - 1)
            visited.remove((coordX, coordY))
            return res
        for r in range(rows):
            for c in range(cols):
                if helper(0, r, c): 
                    return True
        return False


            
            
            
                
            
        