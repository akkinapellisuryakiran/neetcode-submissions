# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        self.values = list()
        self.encode(root)
        return ','.join(self.values)
    
    def encode(self, root):
        if not root:
            self.values.append('#') 
            return
        self.values.append(str(root.val))
        self.encode(root.left)
        self.encode(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))
        def decode() -> Optional[TreeNode]:
            value = next(values)
            if value == '#':
                return None
            node = TreeNode(int(value))
            node.left=decode()
            node.right=decode()

            return node
        return decode()
        