class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if lens != lent:
            return False
        ssplit = []
        tsplit = []
        for i in range(lent):
            ssplit.append(s[i])
            tsplit.append(t[i])
        tsplit.sort()
        ssplit.sort()
        print(ssplit, tsplit)
        if ssplit == tsplit:
            return True
        else:
            return False