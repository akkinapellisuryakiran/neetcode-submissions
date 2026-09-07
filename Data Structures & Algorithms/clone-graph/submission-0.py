"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        original_clone = dict()

        def dfs(original):
            if original in original_clone:
                return original_clone[original]
            copy = Node(original.val)
            original_clone[original] = copy
            for nei in original.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)