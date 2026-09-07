class TrieNode:
    def __init__(self):
        self.children: dict = dict()
        self.end: bool = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
    
        def dfs_search(index, current):
            if index == len(word):
                return current.end
            char = word[index]
            if char == '.':
                for path in current.children.values():
                    if dfs_search(index+1, path):
                        return True
                return False
            if char not in current.children:
                return False
            return dfs_search(index+1, current.children[char])
        return dfs_search(0, current)
        
        

        