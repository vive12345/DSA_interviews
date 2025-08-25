class Solution:
    def helper(self, root, max_dia):
        if not root:
            return 0
        left_height = self.helper(root.left, max_dia)
        right_height = self.helper(root.right, max_dia)
        max_dia[0] = max(max_dia[0], left_height + right_height)
        return max(left_height, right_height) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = [0]  # mutable container
        self.helper(root, max_dia)
        return max_dia[0]
