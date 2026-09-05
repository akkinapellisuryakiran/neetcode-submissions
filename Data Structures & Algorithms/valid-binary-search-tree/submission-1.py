# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_min = float("-inf")
        right_max = float("inf")
        return self.isSubTreeValid(left_min, root, right_max)

    def isSubTreeValid(self, left_min, root, right_max):
        if not root:
            return True
        if left_min >= root.val or root.val >= right_max:
            return False
        return (
            self.isSubTreeValid(left_min, root.left, root.val)
            and
            self.isSubTreeValid(root.val, root.right, right_max)
        )
        