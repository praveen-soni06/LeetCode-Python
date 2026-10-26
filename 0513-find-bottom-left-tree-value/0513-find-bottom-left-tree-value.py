from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        ans = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
            ans.append(current.val)

            if current.right:
                queue.append(current.right)
            
            if current.left:
                queue.append(current.left)

            

        return ans[-1]