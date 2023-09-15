class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rst = 0
        mn = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            else:
                if rst < prices[i] - mn:
                    rst = prices [i] - mn
                
        return rst