class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_operations = 0
        for i in range(1, len(nums), 1):
            if (prev := nums[i-1]) >= nums[i]:
                operations = (prev - nums[i]) + 1
                num_operations += operations
                nums[i] += operations
        return num_operations


