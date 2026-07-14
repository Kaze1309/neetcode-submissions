class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        sa = []
        ta = []
        if sl != tl:
            return False
        for i in range(sl):
            sa.append(s[i])      
            ta.append(t[i])
        sa.sort()
        ta.sort()
        if sa == ta:
            return True
        else:
            return False

