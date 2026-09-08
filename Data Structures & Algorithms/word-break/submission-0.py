class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        dp = [False] * (len(s)+1)
        dp[0] = True
        s_ = len(s)
        for i in range(1, s_+1):
            for word in words:
                len_word = len(word)

                if (
                    len_word <= i
                    and dp[i-len_word]
                    and s[i-len_word:i] == word
                ):
                    dp[i] = True
                    break
        return dp[s_]