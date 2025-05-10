from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        positions = defaultdict(list)


        for s in strs:
            word_count = defaultdict(int)
            for c in s:
                word_count[c] += 1
            key = ""
            for k in sorted(word_count.keys()):
                key = f"{key}{k}{word_count[k]}"
            positions[key].append(s)

        ans = []
        for val in positions.values():
            ans.append(val)
        return ans
        



