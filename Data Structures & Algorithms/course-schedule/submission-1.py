class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        populate an adjacency map:
            {
                course : [prereq, prereq]
            }
        Initialize visited set
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []: if it has no prereqs
                return True
            visited.add(course)
            #if course does have prereqs:
            for prereqs in preMap[course]:
                if not dfs(prereqs):
                    return False

            visited.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            return True
        """
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            #if course is valid but has prereqs
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            #course is completable
            visited.remove(course)
            preMap[course] = [] 
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



        