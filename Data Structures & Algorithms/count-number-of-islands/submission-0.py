class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows_ = len(grid)
        cols_ = len(grid[0])
        island_count = 0
        seen = set()

        def dfs(r,c):
            if not (0<=r<rows_) or not (0<=c<cols_) or grid[r][c] == "0" or (r,c) in seen:
                return
            seen.add((r,c))
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)

        for row in range(rows_):
            for col in range(cols_):
                if grid[row][col] == "1" and (row,col) not in seen:
                    island_count += 1
                    dfs(row,col)
        return island_count
            