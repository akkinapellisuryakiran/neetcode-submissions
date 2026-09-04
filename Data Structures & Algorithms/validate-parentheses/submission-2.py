class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        mapping = {
            ']' : '[',
            '}': '{',
            ')': '('
        }
        close_ = mapping.keys()
        open_ = mapping.values()
        stack = list()

        for symbol in s:
            if symbol in open_:
                stack.append(symbol)
            elif symbol in close_:
                if stack and stack[-1] == mapping[symbol]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True