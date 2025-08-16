class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        print(intervals)
        lastEnd = intervals[0][1]
        countRemove = 0
        for (s, e) in intervals[1:]:
            if s < lastEnd:
                countRemove += 1
                lastEnd = min(e, lastEnd)
            else:
                lastEnd = e
        return countRemove

