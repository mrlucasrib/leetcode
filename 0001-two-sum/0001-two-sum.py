class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            index = diffs.get(target-nums[i], None)
            if index is not None:
                return [index, i]
            diffs[nums[i]] = i
        # for i in range(len(nums)):
        #     index = diffs.get(target-nums[i],None)
        #     if index is not None:
        #         return [i, index]
        