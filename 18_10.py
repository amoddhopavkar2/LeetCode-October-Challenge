# Best Time to Buy and Sell Stock IV

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) <= 1:
            return 0

        if 2 * k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        costs = [float("inf")] * k
        profits = [0] * k
        costs[0] = prices[0]
        profits[0] = 0

        for i in range(1, len(prices)):
            for j in range(k):
                if j == 0:
                    costs[j] = min(costs[j], prices[i])
                    profits[j] = max(profits[j], prices[i]-costs[j])
                else:
                    costs[j] = min(costs[j], prices[i]-profits[j-1])
                    profits[j] = max(profits[j], prices[i]-costs[j])

        return profits[k-1]