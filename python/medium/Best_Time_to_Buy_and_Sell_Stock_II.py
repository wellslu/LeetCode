class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price_a = prices[0]
        for price in prices[1:]:
            if price - price_a > 0:
                profit+=(price - price_a)
            price_a = price
        return profit
