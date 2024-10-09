class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while j > i:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

        
        