from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hm = defaultdict(int)
        ans = []

        for n in nums:
            nums_hm[n] += 1
        bucket = [[] for _ in range(len(nums)+1)]
        
        for num, freq in nums_hm.items():
            bucket[freq].append(num)
        for freq in range(len(nums), 0, -1):
            ans.extend(bucket[freq])

        return ans[:k]
                