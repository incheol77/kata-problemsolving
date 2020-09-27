from typing import List
import collections
import time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NONE, BUY, SELL, COOLDOWN = 'NONE', 'BUY', 'SELL', 'COOL'
        max_profit, tx = 0, NONE
        for i in range(0, len(prices)):
            if tx == NONE and i != len(prices)-1:
                if prices[i] < prices[i+1]:
                    tx = BUY
            elif (tx == BUY or i == len(prices)-1) and prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                tx = SELL
            elif tx == SELL:
                tx = COOLDOWN
            elif tx == COOLDOWN:
                tx = BUY
            print(i, max_profit, tx)

        return max_profit


def main():
    sol = Solution()
    inputs = [[1,2,3,0,2], [1], [1,2,4], [6,1,3,2,4,7]]
    outputs = [3, 0, 3, 6]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maxProfit(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()

