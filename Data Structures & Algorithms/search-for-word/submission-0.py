class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows_ = len(board)
        cols_ = len(board[0])
        word_len = len(word)
        visited = set()

        def dfs(i,j,word_index):
            if word_index == word_len:
                return True
            if (
                not (0 <= i < rows_) 
                or not (0 <= j < cols_)
                or board[i][j] != word[word_index]
                or (i,j) in visited
            ):
                return False
            visited.add((i,j))
            found = (
                dfs(i+1, j, word_index+1) 
                or dfs(i-1, j, word_index+1) 
                or dfs(i, j+1, word_index+1)
                or dfs(i, j-1, word_index+1)
            )
            visited.remove((i,j))
            return found
        
        for i in range(rows_):
            for j in range(cols_):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        
        