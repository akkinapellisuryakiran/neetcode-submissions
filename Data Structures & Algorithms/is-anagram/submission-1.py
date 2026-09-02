from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram_dict = dict()
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        anagram_dict[frozenset(s_dict.items())] = True
        for char in t:
            t_dict[char] += 1
        t_set = frozenset(t_dict.items())
        return anagram_dict.get(t_set, False)
            