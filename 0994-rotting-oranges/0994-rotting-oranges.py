class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq = deque()
        rows, cols = len(grid), len(grid[0])
        mins,fresh = 0,0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    dq.append((row, col, mins))
                elif grid[row][col]==1:
                    fresh+=1
        while dq:
            r, c, mins = dq.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh-=1
                    dq.append((nr, nc,mins+1)) 
        return mins if fresh == 0 else -1 