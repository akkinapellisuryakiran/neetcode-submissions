from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)
        left = 0
        max_freq=0
        answer=0

        for right in range(len(s)):
            char = s[right]
            freq_dict[char]+=1
            max_freq = max(max_freq, freq_dict[char])

            while right-left+1-max_freq > k:
                freq_dict[s[left]]-=1
                left+=1
            answer=max(answer,right-left+1)
        return answer