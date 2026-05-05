class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in h:
                h[key] = [s]
            else:
                h[key].append(s)
        return list(h.values())        