class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        mapp = []
        n = len(nums)
        for num in nums:
            if num not in h:
                h[num]=1
            else:
                h[num] += 1
        for key, v in h.items():
            mapp.append([v,key])
        res = []
        mapp.sort(key= lambda x: x[0], reverse=True)
        for i in range(k):
            res.append(mapp[i][1])
        return res
