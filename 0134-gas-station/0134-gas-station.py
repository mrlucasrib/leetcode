class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        acc = 0
        start = 0
        for i in range(len(gas)):
            realCost = gas[i] - cost[i]
            acc += realCost
            if acc < 0:
                start = i + 1
                acc = 0
        return start
