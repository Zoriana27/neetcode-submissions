class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or heights[r][c] < prevHeight:
                return 
            visited.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col, visited, heights[r][c])


        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        return list(pac & atl)