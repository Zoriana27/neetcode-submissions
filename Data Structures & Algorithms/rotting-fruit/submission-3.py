class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if not q:
            return -1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            count += 1
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
            
        if fresh > 0 or count == 0:
            return -1
        return count - 1