import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # efforts[r][c] will store the minimum effort to reach cell (r, c)
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Min-heap (priority queue) stores (effort, row, col)
        pq = [(0, 0, 0)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            d, r, c = heapq.heappop(pq)
            
            # If we've found a better path to this cell already, skip
            if d > efforts[r][c]:
                continue
            
            # If we've reached the destination, return the effort
            if r == rows - 1 and c == cols - 1:
                return d
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # The effort of this new step
                    step_effort = abs(heights[nr][nc] - heights[r][c])
                    
                    # The total effort for the path to the neighbor
                    # is the max of the path so far and this new step
                    new_effort = max(d, step_effort)
                    
                    # If we found a path with less effort, update and push to pq
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
                        
        return 0 # Should not be reached