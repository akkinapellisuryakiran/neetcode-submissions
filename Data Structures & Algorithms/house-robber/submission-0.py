class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]
        max_rob = [-1] * len(nums)

        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0], nums[1])
        print(max_rob)

        for i in range(2, n):
            max_rob[i] = max(nums[i] + max_rob[i-2], max_rob[i-1])

        return max_rob[-1]
