# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inc = 0
        def g_tree(root):
            nonlocal inc
            if not root :
                return None
            
            g_tree(root.right)
            inc += root.val
            root.val = inc
            g_tree(root.left)
            return root

        return g_tree(root)