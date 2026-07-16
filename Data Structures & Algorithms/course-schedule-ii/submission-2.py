class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {course : [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        visited, visiting = set(), set()
        res = []

        def dfs(course): # course -> bool
            nonlocal res
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for neigh in adj[course]:
                if not dfs(neigh):
                    return False
            
            visiting.discard(course)
            visited.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res[::-1]
