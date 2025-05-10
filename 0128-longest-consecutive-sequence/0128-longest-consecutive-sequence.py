class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        hashset = set(nums)

        for n in hashset:
            if n - 1 not in hashset:
                current_n = n
                current_longest = 1
                while current_n + 1 in hashset:
                    current_n += 1
                    current_longest += 1
                longest = max(longest, current_longest)
        
        return longest
