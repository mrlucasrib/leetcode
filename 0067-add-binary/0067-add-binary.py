from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        ans = deque()
        for i in range(max(len(a), len(b))):
            iA = len(a)-1 - i
            iB = len(b)-1 - i

            bitA = a[iA] if iA >= 0 else "0"
            bitB = b[iB] if iB >= 0 else "0"

            if bitA != bitB:
                if carry == "1":
                    ans.appendleft("0")
                else:
                    ans.appendleft("1")
            else:
                ans.appendleft(carry)
                if bitA == "1":
                    if carry == "0":
                        carry = "1"
                else:
                    carry = "0"
        if carry == "1":
            ans.appendleft("1")
        return "".join(ans)