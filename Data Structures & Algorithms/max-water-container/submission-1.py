class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxx = 0
        while l <= r:
            cur = min(heights[r], heights[l]) * (r - l)
            maxx = max(cur, maxx)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxx
