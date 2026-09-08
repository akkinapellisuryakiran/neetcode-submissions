class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_ = len(s)
        result = ""
        best_len = 0

        def expand(left, right):
            nonlocal result, best_len
            length = 0
            is_even = left == right
            while ( 0<= left
                and right < s_
                and s[left] == s[right]
            ):
                length = right-left+1
                if length > best_len:
                    best_len = length
                    result = s[left:right+1]
                left-=1
                right+=1
  
        for i in range(s_):
            expand(i,i)
            expand(i,i+1)
        return result