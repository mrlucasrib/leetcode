class Solution:
    def findLatestTime(self, s: str) -> str:
        nums = "23456789"
        s = list(s)
        if s[0] == '?':
            s[0] = '0' if s[1] in nums else '1'
        if s[1] == '?':
            s[1] = '1' if s[0] == '1' else '9'
        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'
        return "".join(s)
