class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        if not grid:
            return 0
        
        def dfs(row, col):
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == "0" or (row, col) in visited:
                return 
        
            visited.add((row, col))
            return dfs(row+1, col) or dfs(row, col+1) or dfs(row-1, col) or dfs(row, col-1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands