class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                _row, _col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for direction in directions:
                    r = _row + direction[0]
                    c = _col + direction[1]
                    if (r, c) not in visited and r in range(rows) and c in range(cols) and grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

        