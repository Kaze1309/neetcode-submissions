class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mid = []
        hM = {}
        for strr in strs:
            narr = []
            for char in strr:
                narr.append(char)
            mid.append(narr)
        
        for i in range(len(mid)):
            mid[i].sort()
            mid[i] = "".join(mid[i])
            
        for i in range(len(strs)):
            if mid[i] not in hM:
                hM[mid[i]] = [strs[i]] 
            else:
                hM[mid[i]].append(strs[i])
        return list(hM.values())