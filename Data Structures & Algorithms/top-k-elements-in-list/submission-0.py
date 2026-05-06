class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        sorted_v = list(sorted(h.items(), key=lambda x: x[1], reverse=True))
        res = []
        for i in range(k):
            res.append(sorted_v[i][0])
        return res