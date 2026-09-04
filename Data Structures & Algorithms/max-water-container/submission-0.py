class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1
        left_max = 0
        right_max = 0

        while left<right:
            left_max = max(left_max, heights[left])
            right_max = max(right_max, heights[right])

            max_area = max(max_area, min(left_max, right_max)*abs(right-left))
            if left_max <= right_max:
                left+=1
            else:
                right-=1
        return max_area
        