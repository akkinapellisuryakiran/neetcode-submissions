class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            len_ = len(word)
            encoded_str += str(len_) + '#' + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        s_len = len(s)
        i = 0
        result = list()
        while i < s_len:
            j = i
            while s[j] != '#':
                j+=1
            len_word = int(s[i:j])
            word_start = j+1
            word_end = word_start+len_word
            result.append(s[word_start: word_end])
            i = word_end
        return result