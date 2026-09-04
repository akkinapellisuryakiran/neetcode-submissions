from collections import deque,defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dq = deque([])
        freq_dict = defaultdict(int)
        for num in s:
            if freq_dict[num]==0:
                dq.append(num)
                max_len=max(max_len, len(dq))
                freq_dict[num]+=1
            else:
                while dq:
                    if dq[0] == num:
                        dq.popleft()
                        dq.append(num)
                        break
                    freq_dict[dq[0]]-=1
                    dq.popleft()
                    
        return max_len

                