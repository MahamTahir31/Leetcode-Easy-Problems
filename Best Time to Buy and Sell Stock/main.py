class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell>buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
max_profit = solution.maxProfit(prices)
print(f"Maximum Profit: {max_profit}")
