# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arraytotree(left, right):
            nonlocal preorderIdx
            if left > right:   # base case
                return None

            rootVal = preorder[preorderIdx]  # take value from preorder
            root = TreeNode(rootVal)

            preorderIdx += 1

            root.left = arraytotree(left, inorderHasmap[rootVal] - 1)
            root.right = arraytotree(inorderHasmap[rootVal] + 1, right)

            return root

        preorderIdx = 0
        inorderHasmap = {val: idx for idx, val in enumerate(inorder)}
        return arraytotree(0, len(preorder) - 1)
