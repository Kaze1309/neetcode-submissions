class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h = {}
        freq = [0] * (n + 1)
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        for key, val in h.items():
            if freq[val] == 0:
                freq[val] = [key]
            else:
                freq[val].append(key)

        res = []
        for i in range(n,-1,-1):
            if freq[i] == 0:
                continue
            else:
                res.extend(freq[i])
        return res[0:k]
        