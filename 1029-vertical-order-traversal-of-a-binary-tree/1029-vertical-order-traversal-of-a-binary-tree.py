from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapp = defaultdict(list) 
        dq = deque([(root, 0, 0)])
        
        while dq:
                node, row, col = dq.popleft()
                if not node:
                    continue
                mapp[col].append((row, node.val))

                if node.left:
                    dq.append((node.left, row + 1, col - 1))
                if node.right:
                    dq.append((node.right, row + 1, col + 1))
        
        result = []
        for col in sorted(mapp.keys()):
            nodes = sorted(mapp[col])
            result.append([val for i, val in nodes])
            
        return result