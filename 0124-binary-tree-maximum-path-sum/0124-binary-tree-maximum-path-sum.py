# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            
            if not root:
                return 0
            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))

            res = max(res, left_sum + right_sum + root.val)

            return max(left_sum, right_sum)+ root.val
        dfs(root)
        return res
        