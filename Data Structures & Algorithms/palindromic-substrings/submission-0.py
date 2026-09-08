class Solution:
    def countSubstrings(self, s: str) -> int:
        s_ = len(s)
        count = 0

        def expand(left, right):
            nonlocal count
            while ( 
                0 <= left
                and right < s_
                and s[left] == s[right]
            ):
                count += 1
                left-=1
                right+=1
  
        for i in range(s_):
            expand(i,i)
            expand(i,i+1)
        return count