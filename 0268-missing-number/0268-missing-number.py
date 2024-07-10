class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        real = 0
        for i, n in enumerate(nums):
            expected += i
            real += n
            
        return expected+len(nums) - real


        