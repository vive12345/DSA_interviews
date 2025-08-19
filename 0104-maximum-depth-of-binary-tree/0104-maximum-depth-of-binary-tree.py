# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def samelevel(self, root, depth, max_res):
        '''
        O(n) tc as we go trough all the elements from the root which is n
        sc in worst case can be a skweed tree whihc is O(n) or else the tree's height in normal case could be logn - perfect binary tree.
        '''
        if not root:
            return
        # update max depth
        max_res[0] = max(max_res[0], depth)

        # go left and right with +1 depth
        self.samelevel(root.left, depth + 1, max_res)
        self.samelevel(root.right, depth + 1, max_res)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_res = [0]   # use list so it’s mutable
        self.samelevel(root, 1, max_res)
        return max_res[0]
