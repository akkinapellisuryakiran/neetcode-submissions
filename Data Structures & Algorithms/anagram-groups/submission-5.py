from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        
        anagram_dict = defaultdict(list)
        ord_a = ord('a')
        for single_str in strs:
            count = [0] *26
            for char in single_str:
                count[ord(char)-ord_a] += 1      
            anagram_dict[tuple(count)].append(single_str)
        # print(anagram_dict)
        return list(anagram_dict.values())
