class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        
        ss = s.lower()
        sss = ""
        for char in ss:
            if char.isalnum():
                sss += char

        r = len(sss) - 1 
        while l <= r:
            if sss[l] == sss[r]:
                l += 1
                r -= 1
            else:
                return False

        return True