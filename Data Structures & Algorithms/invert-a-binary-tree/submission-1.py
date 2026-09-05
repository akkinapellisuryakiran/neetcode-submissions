# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertSubTree(root)
        return root
    def invertSubTree(self, parent):
        if not parent:
            return
        self.invertSubTree(parent.left)
        self.invertSubTree(parent.right)
        parent.left, parent.right = parent.right, parent.left
