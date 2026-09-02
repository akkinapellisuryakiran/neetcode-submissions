class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_dict = dict()
        for index_, num in enumerate(nums):
            item = target - num
            if item in nums_index_dict:
                return [nums_index_dict[item], index_]
            nums_index_dict[num] = index_
        