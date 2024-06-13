class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        downBound, rightBound, leftBound, upperBound = len(matrix)-1, len(matrix[0])-1, 0, 0
        i,j = 0,0
        dr, dc = 0,1
        while len(ans) < len(matrix) * len(matrix[0]):
            ans.append(matrix[i][j])
            i += dr
            j += dc
            if j > rightBound:
                dr, dc = 1, 0
                i +=1
                j -=1
                upperBound += 1
            elif i > downBound:
                dr, dc = 0, -1
                i -= 1
                j -= 1
                rightBound -= 1
            elif j < leftBound:
                dr, dc = -1, 0
                i -= 1
                j += 1
                downBound -= 1
            elif i < upperBound:
                dr, dc = 0, 1
                i += 1
                j += 1
                leftBound += 1
        return ans