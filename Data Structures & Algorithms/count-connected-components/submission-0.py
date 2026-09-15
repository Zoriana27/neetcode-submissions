class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        visited = set()
        count = 0
        def dfs(node):  
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count

            


        