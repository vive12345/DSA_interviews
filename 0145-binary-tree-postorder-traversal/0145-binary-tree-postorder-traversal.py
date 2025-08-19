# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, res, root):
        if not root:
            return 
        self.postorder(res, root.left)
        self.postorder(res, root.right)
        res.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(res, root)
        return res
        
        