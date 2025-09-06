# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.pop()
                if node.left: dq.appendleft(node.left)
                if node.right: dq.appendleft(node.right)
            res.append(node.val)
        return res