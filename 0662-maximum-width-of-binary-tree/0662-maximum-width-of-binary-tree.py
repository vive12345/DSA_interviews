# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # The initial item must be a tuple in a list.
        dq = deque([(root, 0)])
        maxWidth = 0

        while dq:
            # FGet the length *before* the loop.
            level_length = len(dq)

            _, levelStart = dq[0]

            for i in range(level_length):
                node, index = dq.popleft()

                if node.left:
                    dq.append((node.left, 2 * index))
                if node.right:
                    dq.append((node.right, 2 * index + 1))

            maxWidth = max(maxWidth, index - levelStart + 1)

        return maxWidth