class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        cursorS = 0
        cursorT = 0
        s = list(s)
        t = list(t)
        print(s, t)
        lettersS = []
        lettersT = []
        while len(s) > cursorS or len(t) > cursorT:
            if cursorS < len(s) and s[cursorS] == "#":
                if len(lettersS) > 0:
                    lettersS.pop()
            elif cursorS < len(s) and s[cursorS] != "#":
                lettersS.append(s[cursorS])
            if cursorT < len(t) and t[cursorT] == "#":
                if len(lettersT) > 0:
                    lettersT.pop()
            elif cursorT < len(t) and t[cursorT] != "#":
                lettersT.append(t[cursorT])
            cursorS += 1
            cursorT += 1
        if len(lettersS) != len(lettersT):
            return False
        for ns, nt in zip(lettersS, lettersT):
            if ns != nt:
                return False
        return True
