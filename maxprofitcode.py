def maxProfit(prices):
    max_profit = 0
    i = 0
    j = 0
    while j < len(prices):
        if prices[j] < prices[i]:
            i = j
        else:
            max_profit = max(max_profit, (prices[j] - prices[i]))
        j += 1
    return max_profit