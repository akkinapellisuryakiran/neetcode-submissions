class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float("-inf")
        current = float("-inf")
        for num in nums:
            current = max(num, num+current)
            max_ = max(max_,current)
        return max_