class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        # adj is the adjacency list: prereq -> [courses that depend on it]
        adj = [[] for _ in range(numCourses)]
        # in_degree counts how many prerequisites each course has
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        # Step 2: Initialize the queue with courses that have no prerequisites
        dq = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        # Step 3: Process the courses (BFS)
        while dq:
            # Dequeue a course that is ready to be taken
            course = dq.popleft()
            ans.append(course)

            # For each neighbor, reduce its in-degree because we've completed a prerequisite
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                
                # If the neighbor has no more prerequisites, it's ready to be taken
                if in_degree[neighbor] == 0:
                    dq.append(neighbor)

        # Step 4: Check if we were able to finish all courses
        # If the length of the order matches numCourses, we have a valid order.
        # Otherwise, there was a cycle, and it's impossible.
        if len(ans) == numCourses:
            return ans
        else:
            return []

        