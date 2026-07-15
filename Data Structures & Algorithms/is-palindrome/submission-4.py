class Solution:
    def isPalindrome(self, s: str) -> bool:
        sa = []
        for char in s:
            if char.isalnum():
                sa.append(char)
        ss = "".join(sa).lower()
        l = 0
        r = len(ss) - 1
        print(sa)
        print(ss)
        while l <= r:
            if ss[l] == ss[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True
