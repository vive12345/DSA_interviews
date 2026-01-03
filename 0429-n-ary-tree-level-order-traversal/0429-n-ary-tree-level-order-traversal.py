"""
# Definition for a Node.

from typing import Optional, List
from collections import deque
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution: 
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        ans=[]
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                dq.extend(node.children)
            ans.append(level)
        return ans

#     def levelordertravese(self, arr: List[Optional[int]]) -> Optional[Node]:
#         if not arr:
#             return None
#         root = Node(arr[0])
#         q = deque([root])
#         i = 1
#         if i < len(arr) and arr[i] is None:
#             i += 1
#         while q and i < len(arr):
#             parent = q.popleft()
#             children = []
#             while i < len(arr) and arr[i] is not None:
#                 child =  Node(arr[i], [])
#                 children.append(child)
#                 q.append(child)
#                 i += 1
#             parent.children = children
#             i += 1  # skip the None separator
#         return root
        
# s = Solution()
# root = s.levelordertravese([1,None,3,2,4,None,5,6])
# ans = s.levelOrder(root)
# print(ans)
