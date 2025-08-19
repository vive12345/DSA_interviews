# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time: O(n) → every node is visited once.
    Space: O(h) for recursion stack (h = height of tree). Worst case O(n) for skewed tree.
    '''
    def preorder(self, res, root):
            if root:
                res.append(root.val)
                self.preorder(res, root.left)
                self.preorder(res, root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder(res, root)
        return res
        
    
        