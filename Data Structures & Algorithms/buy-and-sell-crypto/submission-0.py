class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b = 0
        maxp = 0
        s = 1
        while s < n:
            curp = prices[s] - prices[b]
            if curp < 0:
                b = s
            else:
                if curp >= maxp:
                    maxp = curp
            s += 1 
            
        return maxp
