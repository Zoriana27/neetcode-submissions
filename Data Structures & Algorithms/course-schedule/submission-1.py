class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPrereq = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crsToPrereq[crs].append(prereq)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crsToPrereq[crs] == []:
                return True
            visited.add(crs)
            for prereq in crsToPrereq[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            crsToPrereq[crs] = []
            return True
        for crs in crsToPrereq:
            if not dfs(crs): return False
        return True        