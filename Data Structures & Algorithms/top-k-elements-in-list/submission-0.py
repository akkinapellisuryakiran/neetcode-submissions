from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        freq_heap = list()
        for num, freq in freq_dict.items():
            if len(freq_heap) < k:
                heapq.heappush(freq_heap, (freq, num))
            elif freq > freq_heap[0][0]:
                heapq.heappop(freq_heap)
                heapq.heappush(freq_heap, (freq, num))
        result = list()
        while freq_heap:
            result.append(heapq.heappop(freq_heap)[1])
        return result


