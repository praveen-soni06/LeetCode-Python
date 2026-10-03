# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(curr, nums):

            if not curr:
                return 0 
            nums = nums * 10 + curr.val # curr.val = 4 then it become 40 so it handel the numbe 
            if not curr.left and not curr.right: # if reach to the leaf return the root to leaf like 495
                return nums  
            return dfs(curr.left, nums) + dfs(curr.right, nums) # return the sum of root -> leaf 495 + 491 like this
        return dfs(root,0)