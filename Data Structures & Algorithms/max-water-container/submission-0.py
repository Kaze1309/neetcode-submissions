class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_cap = -1
        while l < r:
            if heights[l] < heights[r]:
                res = heights[l] * (r - l)
                l += 1
            else:
                res = heights[r] * (r - l)
                r -= 1
            if res > max_cap:
                max_cap = res
        
        return max_cap
