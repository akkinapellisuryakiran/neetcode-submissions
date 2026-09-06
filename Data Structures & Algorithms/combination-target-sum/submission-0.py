class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = list()
        path = list()
        len_=len(nums)

        def dfs(i, total):
            if total == target:
                results.append(path.copy())
                return
            
            if i>=len_ or total>target:
                return
            
            path.append(nums[i])
            dfs(i, nums[i]+total)
            path.pop()
            dfs(i+1, total)
        dfs(0,0)
        return results

