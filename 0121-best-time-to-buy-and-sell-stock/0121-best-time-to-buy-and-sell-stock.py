class Solution(object):
    def maxProfit(self, prices):
        l=0
        profit = 0
        maxP = 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            else:
                l = r

        return maxP