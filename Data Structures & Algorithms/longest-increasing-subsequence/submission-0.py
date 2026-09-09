class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for num in nums:
            left = 0
            right = len(dp)

            while left < right:
                mid = left + (right-left)//2
                if dp[mid] < num:
                    left = mid+1
                else:
                    right = mid
            if left == len(dp):
                dp.append(num)
            else:
                dp[left] = num
        return len(dp)