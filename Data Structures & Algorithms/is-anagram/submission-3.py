class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shash = {}
        thash = {}
        for c in s:
            if c not in shash:
                shash[c] = 1
            else:
                shash[c] += 1
        for c in t:
            if c not in thash:
                thash[c] = 1
            else:
                thash[c] += 1
        for key in shash:
            if key in thash:
                if shash[key] == thash[key]:
                    continue
                return False
            return False
        return True

