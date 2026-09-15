class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        visitedPath = set()

        def dfs(current, previous):
            if current in visitedPath:
                return False
            visitedPath.add(current)
            for neighbour in adjList[current]:
                if neighbour == previous:
                    continue
                if not dfs(neighbour, current):
                    return False
            return True

        return dfs(0, -1) and n == len(visitedPath)

        