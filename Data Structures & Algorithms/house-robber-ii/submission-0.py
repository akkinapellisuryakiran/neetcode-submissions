class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def solve(houses):
            prev2 = 0
            prev1 = 0
            for house in houses:
                current = max(
                    prev1,
                    house + prev2
                )
                prev2 = prev1
                prev1 = current
            return prev1
        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )