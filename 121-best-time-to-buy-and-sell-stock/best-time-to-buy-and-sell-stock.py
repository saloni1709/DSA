class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit