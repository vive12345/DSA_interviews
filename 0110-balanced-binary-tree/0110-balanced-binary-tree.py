# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, res):
        if not root:
            return 0
        left_height = self.helper(root.left, res)
        right_height = self.helper(root.right, res)
        if abs(left_height - right_height) > 1:
            res[0] = False
        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]   # use list so it’s mutable
        self.helper(root, res)
        return res[0]
