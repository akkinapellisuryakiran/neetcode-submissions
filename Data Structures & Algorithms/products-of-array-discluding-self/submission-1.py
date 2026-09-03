class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if  len(nums) <= 1:
            return []
        prefix_list = [1] * len(nums)
        len_ = len(nums)
        prefix = 1
        for i in range(len_):
            prefix_list[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        suffix_list = [1] * len(nums)
        for i in range(len_-1,-1,-1):
            suffix_list[i] = suffix
            suffix *= nums[i]
        
        return [prefix_list[i]*suffix_list[i] for i in range(len_)]

        