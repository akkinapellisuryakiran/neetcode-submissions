from collections import deque,defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dq = deque([])
        freq_dict = defaultdict(int)
        for num in s:
            if freq_dict[num]==0:
                dq.append(num)
                freq_dict[num]+=1
            else:
                while dq:
                    removed = dq.popleft()
                    freq_dict[removed]-=1
                    if removed == num:
                        break
                dq.append(num)
                freq_dict[num]+=1
            max_len=max(max_len, len(dq))
                    
        return max_len

                