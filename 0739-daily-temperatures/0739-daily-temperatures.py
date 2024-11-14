class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()

            if stack:
                elem = stack[-1]
                stack.append((temperatures[i], i))
                temperatures[i] = elem[1] - i

            else:
                stack.append((temperatures[i], i))
                temperatures[i] = 0
        return temperatures
