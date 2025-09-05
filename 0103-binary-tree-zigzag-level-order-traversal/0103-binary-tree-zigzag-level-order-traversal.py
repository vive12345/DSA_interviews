# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        counter = 0
        if not root :
            return []
        res, dq, flag, = [], deque([root]), True
        while dq:
            level=[]
            for _ in range(len(dq)):
                if flag:
                    node = dq.popleft()
                    level.append(node.val)
                    if node.left: dq.append(node.left)
                    if node.right: dq.append(node.right)
                else:
                    node = dq.pop()
                    level.append(node.val)
                    if node.right: dq.appendleft(node.right)
                    if node.left: dq.appendleft(node.left)
            res.append(level)
            flag = not flag
        return res

        
        