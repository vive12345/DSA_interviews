import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # 1. Edge Case: Check if start or end points are blocked.
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # 2. Initialize the queue for BFS. It stores (row, col, distance).
        queue = collections.deque([(0, 0, 1)]) # Start at (0,0) with path length 1.
        grid[0][0] = 1 # Mark the starting cell as visited.

        # 3. Define the 8 directions for movement.
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # 4. Start the BFS traversal.
        while queue:
            r, c, distance = queue.popleft()

            # 5. Check if we have reached the destination.
            if r == n - 1 and c == n - 1:
                return distance

            # 6. Explore all 8 neighbors.
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # Check if the neighbor is valid:
                # - Within grid boundaries
                # - Is a clear path (value is 0)
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    # Mark as visited
                    grid[new_r][new_c] = 1
                    # Enqueue the neighbor with the new distance
                    queue.append((new_r, new_c, distance + 1))

        # 7. If the queue becomes empty and we haven't reached the end, no path exists.
        return -1
