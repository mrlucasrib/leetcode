class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(i, j, 0, set()):
                    return True
        return False

    def backtracking(self, i, j, indexWord, visited):
        if indexWord == len(self.word):
            return True
        if (i, j) in visited or not self.in_bounds(i, j):
            return False
        if self.board[i][j] != self.word[indexWord]:
            return False

        visited.add((i, j))
        for k, l in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if self.backtracking(k, l, indexWord + 1, visited):
                return True
        visited.remove((i,j))
        return False


    def in_bounds(self, i, j):
        x, y = len(self.board), len(self.board[0])
        return 0 <= i < x and 0 <= j < y
