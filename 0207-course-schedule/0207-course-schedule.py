class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        ans, dq = [], deque()
        for courses, pre in prerequisites:
            adj[pre].append(courses)
            in_degree[courses]+=1
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        while dq:
            course = dq.popleft()
            ans.append(course)
            for dependencies in adj[course]:
                in_degree[dependencies]-=1
                if in_degree[dependencies] == 0 :
                    dq.append(dependencies)
        if len(ans) == numCourses:
            return True
        else:
            return False