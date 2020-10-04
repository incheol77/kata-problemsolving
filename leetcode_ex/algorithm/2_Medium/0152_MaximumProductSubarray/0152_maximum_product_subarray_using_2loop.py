from typing import List
import sys
import time

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prod, max_prod = 1, -sys.maxsize-1
        for start in range(len(nums)):
            prod = 1
            for end in range(start, len(nums)):
                prod *= nums[end]
                max_prod = max(max_prod, prod)
        return max_prod


def main():
    sol = Solution()
    inputs = [[2,3,-2,4], [-2,0,-1], [0,2]]
    outputs = [6, 0, 2]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maxProduct(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


