from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        
        anagram_dict = defaultdict(list)

        for single_str in strs:
            temp_dict = defaultdict(int)
            for char in single_str:
                temp_dict[char] += 1
            set_ = frozenset(temp_dict.items())
            anagram_dict[set_].append(single_str)
        # print(anagram_dict)
       
        return list(anagram_dict.values())
