class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = {}
        maxN = 0
        for i in range(len(nums)):
            maxN = max(maxN, self.backtracking(i, nums))
        return maxN

    def backtracking(self, index, nums):
        if index in self.dp:
            return self.dp[index]
        acc = nums[index]
        for i in range(len(nums) - 1, index + 1, -1):
            acc = max(acc, nums[index] + self.backtracking(i, nums))

        self.dp[index] = acc
        return acc
