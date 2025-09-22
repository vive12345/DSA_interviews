# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        def letsbuildBST(lower, upper):
            if self.idx >= len(preorder) or not (lower < preorder[self.idx] <upper):
                return None
            node_val = preorder[self.idx]
            node = TreeNode(node_val)
            self.idx+=1
            node.left = letsbuildBST(lower, node_val)
            node.right = letsbuildBST(node_val, upper)
            return node
        return letsbuildBST(float('-inf'), float('inf'))
        