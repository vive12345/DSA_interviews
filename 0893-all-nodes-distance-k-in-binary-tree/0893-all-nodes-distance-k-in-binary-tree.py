# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parents(curr, parent): # this will add a parent so we can go up in tree
            if curr:
                curr.parent = parent
                add_parents(curr.left, curr)
                add_parents(curr.right, curr)

        add_parents(root, parent=None)
        res = []
        visited = set()
        def dfs(curr, distance):
            if not curr or curr in visited:
                return
            visited.add(curr)
            if distance == 0:
                res.append(curr.val)
                return
            # these 3 lines - first it will go to target's parents and it travese all the way to the anoter branch until distance or already visisted or None. its recusrions once a condition is meet the control would be returned 
            dfs(curr.parent, distance-1)
            dfs(curr.left, distance-1)
            dfs(curr.right, distance-1)

        dfs(target, k)
        return res
