class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        toggle = True
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sum3 = nums[left] + nums[right] + nums[i]
                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    solutions.append([nums[left], nums[right], nums[i]])
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return solutions
        