# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time complexity: O(n)
    Space complexity: O(n) - In the worst case, we have skewed tree.
    '''
    def inorder(self, res, root):
            if not root:
                return
            self.inorder(res, root.left)
            res.append(root.val)
            self.inorder(res, root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(res, root)
        return res 
        

            

        