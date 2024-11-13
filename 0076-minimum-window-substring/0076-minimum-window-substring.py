from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        ans_length = len(s)
        countT = Counter(t)
        need, have = len(countT), 0
        ans_lr = []
        count_window = defaultdict(int)

        while r < len(s) or (have == need and l <= r):
            if need == have:
                if ans_length >= r - l:
                    ans_lr = [l, r]
                    ans_length = r - l
                count_window[s[l]] -= 1
                if count_window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            else:
                if r >= len(s):
                    break
                letter = s[r]
                count_window[letter] += 1
                if countT[letter] == count_window[letter]:
                    have += 1
                r += 1
        if len(ans_lr) == 0:
            return ""
        return "".join([s[c] for c in range(ans_lr[0], ans_lr[1])])
