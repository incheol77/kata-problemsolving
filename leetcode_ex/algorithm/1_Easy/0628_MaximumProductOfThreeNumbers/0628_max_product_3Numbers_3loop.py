from typing import List
import sys
import time

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        max_prod = -sys.maxsize-1
        for x in range(len(nums)-2):
            for y in range(x+1, len(nums)-1):
                for z in range(y+1, len(nums)):
                    max_prod = max(max_prod, nums[x]*nums[y]*nums[z])
        return max_prod


def main():
    sol = Solution()
    inputs = [[1,2,3], [1,2,3,4]]
    outputs = [6, 24]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maximumProduct(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


