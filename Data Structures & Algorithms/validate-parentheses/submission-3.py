class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        mapping = {
            ']' : '[',
            '}': '{',
            ')': '('
        }
        stack = list()

        for symbol in s:
            if symbol in mapping:
                if not stack:
                    return False
                if stack.pop() != mapping[symbol]:
                    return False  
            else:
                stack.append(symbol)
        if stack:
            return False
        return True