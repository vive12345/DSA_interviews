from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        
        if not (0 <= sr < rows and 0 <= sc < cols):
            return image   # invalid start, just return unchanged

        start_color = image[sr][sc]
        if start_color == color:   # nothing to do
            return image

        dq = deque([(sr, sc)])
        image[sr][sc] = color

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                    image[nr][nc] = color
                    dq.append((nr, nc))

        return image
