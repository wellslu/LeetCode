class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_index = len(prices) - 1 - prices[::-1].index(max(prices))
        if max_index == 0:
            min_num = prices[0]
            maxprofit = 0
        else:
            min_num = min(prices[:max_index])
            maxprofit = prices[max_index] - min_num
        for price in prices[max_index:]:
            if price - min_num > maxprofit:
                maxprofit = price - min_num
            elif price < min_num:
                min_num = price
        return maxprofit
