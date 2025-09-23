# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dq = deque([root])
        seen = set()
        while dq:
            node = dq.popleft()
            compliment = k - node.val
            if compliment in seen:
                return True
            seen.add(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return False
            
        