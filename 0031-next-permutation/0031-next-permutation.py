class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        if pivot != -1:
            for i in range(len(nums)-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        


        
        