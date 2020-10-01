import time
from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        max_price = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                max_price = max(max_price, prices[j] - prices[i])
        return max_price


def main():
    inputs = [[7,1,5,3,6,4], [7,6,4,3,1]]
    outputs = [5, 0]
    sol = Solution()
    for i in range(len(inputs)):
        start = time.time()
        res = sol.max_profit(inputs[i])
        end = time.time()
        if outputs[i] == res :
            print(True, " : ", end-start, " sec")
        else:
            print(False, " : ", end-start, " sec")


if __name__ == "__main__":
    main()

