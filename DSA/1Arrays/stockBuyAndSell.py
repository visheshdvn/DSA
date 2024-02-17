def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])

    return profit


prices = [int(i) for i in input().split()]
print("Max profit:", max_profit(prices))
