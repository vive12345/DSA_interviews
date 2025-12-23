from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or len(graph) == 0:
            return paths
        path = [0]
        dq = deque()
        dq.append(path)
        while dq:
            currpath = dq.popleft()
            node = currpath[-1]
            for next_node in graph[node]:
                temppath = currpath.copy()
                temppath.append(next_node)

                if next_node == len(graph)-1:
                    paths.append(temppath)
                else:
                    dq.append(temppath)
        return paths


