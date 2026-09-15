class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrerequisites = {i:[] for i in range(numCourses)}
        visitedPath = set()
        for course, prerequisite in prerequisites:
            courseToPrerequisites[course].append(prerequisite)

        def dfs(course):
            if course in visitedPath:
                return False
            if courseToPrerequisites[course] == []:
                return True
            visitedPath.add(course)
            for prerequisite in courseToPrerequisites[course]:
                if not dfs(prerequisite): #if cycle
                    return False
            visitedPath.remove(course)
            courseToPrerequisites[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i): #if cycle
                return False
        return True
            
            

        