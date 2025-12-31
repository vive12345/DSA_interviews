from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        dq = deque([(0, 0, 1)])  # (r, c, distance)
        visited = {(0, 0)}

        while dq:
            r, c, dist = dq.popleft()
            if r == n-1 and c == n-1:
                return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    dq.append((nr, nc, dist + 1))
        return -1

# s = Solution()
# ans = s.shortestPathBinaryMatrix([[0,1],[1,0]])
# print(ans)