class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.letters = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        combinations = []
        self.backtracking(0, [], digits, combinations)
        return combinations
    
    def backtracking(self, depth, currentComb, digits, combinations):
        if depth == len(digits):
            combinations.append("".join(currentComb))
            currentComb.pop()
            return

        for letter in self.letters[int(digits[depth])]:
            currentComb.append(letter)
            self.backtracking(depth+1, currentComb, digits, combinations)
        if currentComb: currentComb.pop()

