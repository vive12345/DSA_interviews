
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        level_start = root
        while level_start.left:
            curr = level_start
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            level_start = level_start.left
        return root

#     def constructgraph(self, arr):
#         if not arr:
#             return None
#         nodes = [None if v is None else Node(v) for v in arr]
#         i, j = 0, 1
#         while j < len(nodes):
#             if nodes[i]:
#                 nodes[i].left = nodes[j] if j < len(nodes) else None
#                 nodes[i].right = nodes[j+1] if j+1 < len(nodes) else None
#                 j+=2
#             i+=1
#         return nodes[0]
        
#     def serialize_by_next(self,root):
#         if not root:
#             return []
#         res = []
#         levelstart = root
#         while levelstart:
#             curr = levelstart
#             while curr:
#                 res.append(curr.val)
#                 curr = curr.next
#             res.append('#')
#             levelstart = levelstart.left
#         return res
  
# s = Solution()
# root = s.constructgraph([1,2,3,4,5,6,7,8])
# s.connect(root)
# print(s.serialize_by_next(root))