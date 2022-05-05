def solution(A):
    # write your code in Python 3.6
    maxProfit = 0
    for purchaseDate in range(len(A)):
        for sellDate in range(purchaseDate, len(A)):
            profitLoss = A[sellDate]-A[purchaseDate]
            if profitLoss > maxProfit:
                maxProfit = profitLoss
    return maxProfit
