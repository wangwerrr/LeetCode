class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(minPrice, price)   # deciding buying price
            maxProfit = max(maxProfit, price - minPrice) # for a given buying price, find the selling price(after buying price) which maximize the profit
        return maxProfit
