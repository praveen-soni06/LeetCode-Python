# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        arr= []
        def pre_order(root):
            if not root:
                return None
            arr.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

            return root
        pre_order(root)
        return arr