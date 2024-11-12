from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        countS = Counter(s[:len(p)])
        l = 0
        ans = []
        if countP == countS:
            ans.append(0)
        for r in range(len(p), len(s)):
            countS[s[r]] += 1
            countS[s[l]] -= 1
            if countS[s[l]] == 0:
                del countS[s[l]]
            l +=1

            if countS == countP:
                ans.append(l)
        return ans


            
        