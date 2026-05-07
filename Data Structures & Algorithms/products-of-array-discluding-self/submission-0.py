class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        res = []
        for i in range(n):
            if i == 0:
                pref[i] = nums[i]
            pref[i] = pref[i-1] * nums[i]
        for i in range(n-1,-1,-1):
            if i == n-1:
                suff[i] = nums[i]
            else:
                suff[i] = suff[i+1] * nums[i]
        for i in range(n):
            if i == 0:
                res.append(1 * suff[i+1])
            elif i == n-1:
                res.append(1 * pref[i-1])
            else:
                res.append(pref[i-1] * suff[i+1])
        return res