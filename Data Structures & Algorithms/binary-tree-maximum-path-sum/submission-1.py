# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.calculate(root)
        return self.max_sum
    
    def calculate(self, root) -> int:
        # nonlocal max_sum
        if not root:
            return 0
        left = max(0, self.calculate(root.left))
        right = max(0, self.calculate(root.right))

        self.max_sum = max(
            self.max_sum, 
            left + root.val + right
        )

        return root.val + max(left,right)
