class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build Trie for words
        root = TrieNode()

        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.word = word
        
        
        rows_ = len(board)
        cols_ = len(board[0])
        result = list()
        # do dfs on board and find words
        def dfs(r, c, node):
            if not 0<=r<rows_ or not 0<=c<cols_:
                return
            char = board[r][c]
            if char == '#' or char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None
            board[r][c] = '#'

            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)
            dfs(r-1, c, next_node)
            dfs(r+1, c, next_node)

            board[r][c] = char

        for r in range(rows_):
            for c in range(cols_):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return result
        

                