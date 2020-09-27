from typing import List
import collections
import time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit


def main():
    sol = Solution()
    inputs = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]]
    outputs = [7,4,0]

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

