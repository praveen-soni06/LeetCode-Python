# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        
        rv = []

        def dfs(root, level):
            if not root: return

            if level == len(rv):   # check level wise and print if right present print that and ignore left side
                rv.append(root.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root,0)
        return rv