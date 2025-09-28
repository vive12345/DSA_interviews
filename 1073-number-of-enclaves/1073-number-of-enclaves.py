class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dq = deque()
        seen = set()
        counter = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows-1 or col == 0 or col == cols-1) and grid[row][col] == 1:
                    dq.append((row, col))
                    seen.add((row, col))
        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 1:
                    seen.add((nr, nc))
                    dq.append((nr, nc))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and (row, col) not in seen :
                    seen.add((row, col))
                    counter+=1
        return counter