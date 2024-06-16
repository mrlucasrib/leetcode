class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countStop = [False, False, False, False]
        tFirst, bFirst = tops[0], bottoms[0]
        counterTopInTop = 0
        counterTopInBottom = 0
        countBotInTop = 0
        countBotInBot = 0
        for i in range(len(tops)):
            # All tFist in tops
            if tFirst == bottoms[i] and tops[i] != bottoms[i]:
                counterTopInTop += 1
            elif tFirst != tops[i]:
                countStop[0] = True
            # All tFirsts in bottoms
            if tFirst == tops[i] and tops[i] != bottoms[i]:
                counterTopInBottom += 1
            elif tFirst != bottoms[i]:
                countStop[1] = True
            # All bFirsts in tops
            if bFirst == bottoms[i] and tops[i] != bottoms[i]:
                countBotInTop += 1
            elif bFirst != tops[i]:
                countStop[2] = True
            # All bFirsts in buttoms
            if bFirst == tops[i] and tops[i] != bottoms[i]:
                countBotInBot += 1
            elif bFirst != bottoms[i]:
                countStop[3] = True
            if all(countStop):
                return -1

        minExcept0 = [
            v
            for i, v in enumerate(
                [counterTopInTop, counterTopInBottom, countBotInTop, countBotInBot]
            )
            if not countStop[i]
        ]
        print(minExcept0)
        if len(minExcept0) == 0:
            return 0
        return min(minExcept0)
