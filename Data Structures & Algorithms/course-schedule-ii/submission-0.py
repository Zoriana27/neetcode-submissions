class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsToPrereq = {c:[] for c in range(numCourses)}
        for crs, prereq in prerequisites:
            crsToPrereq[crs].append(prereq)

        visited = set()
        cycle = set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for prereq in crsToPrereq[crs]:
                if not dfs(prereq):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for crs in crsToPrereq:
            if not dfs(crs):
                return []
        return output