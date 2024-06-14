class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for num in nums:
            elements.add(num)
        return len(elements) != len(nums)
        