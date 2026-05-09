class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for char in s:
            if char in "0123456789" or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122: 
                check += char
        l = 0
        r = len(check) - 1
        tocheck = check.lower()
        while l <= r:
            if tocheck[l] == tocheck[r]:
                l+= 1
                r -= 1
                continue
            else:
                return False
            l += 1
            r -= 1
        return True 