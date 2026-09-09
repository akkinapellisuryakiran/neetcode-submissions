class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i, n in enumerate(nums):
            result = result ^ i
            result = result ^ n
        return result