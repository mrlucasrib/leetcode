class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        sl = list(s)
        while l < r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
        return "".join(sl)
        