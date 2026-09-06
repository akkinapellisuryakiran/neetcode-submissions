import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.right and -self.left[0] > self.right[0]:
            pop_num = -heapq.heappop(self.left)
            heapq.heappush(self.right, pop_num)
        if len(self.left) > len(self.right) + 1:
            pop_num = -heapq.heappop(self.left)
            heapq.heappush(self.right, pop_num)
        elif len(self.right) > len(self.left):
            pop_num = -heapq.heappop(self.right)
            heapq.heappush(self.left, pop_num)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0])/2
        return -self.left[0]
        