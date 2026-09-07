class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows_ = len(heights)
        cols_ = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, seen, prev):
            if (
                not (0<=r<rows_)
                or not (0<=c<cols_)
                or (r,c) in seen
                or heights[r][c] < prev
            ):
                return
            seen.add((r,c))
            height = heights[r][c]

            dfs(r, c-1, seen, height)
            dfs(r, c+1, seen, height)
            dfs(r-1, c, seen, height)
            dfs(r+1, c, seen, height)
        
        # pacific left
        for c in range(cols_):
            dfs(0, c, pacific, float("-inf"))
        
        # pacific top
        for r in range(rows_):
            dfs(r, 0, pacific, float("-inf"))
        
        # atlantic bottom
        for c in range(cols_):
            dfs(rows_-1, c, atlantic, float("-inf"))

        # atlantic right
        for r in range(rows_):
            dfs(r, cols_-1, atlantic, float("-inf"))
        
        return list(pacific & atlantic)
