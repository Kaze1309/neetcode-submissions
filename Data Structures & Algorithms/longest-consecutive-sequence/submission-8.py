class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        h = {}
        nums = set(nums)
        if n == 0:
            return 0
        for num in nums:
            if num - 1 not in nums:
                h[num] = 1
        starters = list(h.keys())

        for num in nums:
            if num in starters :
                nxt = num + 1
                while nxt in nums:
                        h[num] += 1
                        nxt += 1
        return max(h.values())
