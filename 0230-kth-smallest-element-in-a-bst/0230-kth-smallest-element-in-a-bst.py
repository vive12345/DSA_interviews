# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.counter=0
        def helper(node):
            if not node or self.ans is not None:
                return
            helper(node.left)
            self.counter+=1
            if self.counter == k :
                self.ans = node.val
                return
            helper(node.right)
            
        helper(root)
        return self.ans
           
        