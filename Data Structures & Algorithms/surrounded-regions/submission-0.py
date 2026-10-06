class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row == rows - 1 or col == cols - 1 or row == 0 or col == 0):
                    q.append((row, col))
                    board[row][col] = "V"
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row < 0 or row == rows or col < 0 or col == cols or board[row][col] != "O":
                    continue
                    
                q.append((row, col))
                board[row][col] = "V"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "V":
                    board[r][c] = "O"

                
            

        