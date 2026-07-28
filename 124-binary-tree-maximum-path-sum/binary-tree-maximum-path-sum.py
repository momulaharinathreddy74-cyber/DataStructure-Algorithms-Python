# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max1=float('-inf')
        def solver(root):
            nonlocal max1
            if not root:
                return 0
            left=max(0,solver(root.left))
            right=max(0,solver(root.right))
            max1=max(max1,root.val+left+right)
            return root.val+max(left,right)
        solver(root)
        return max1

