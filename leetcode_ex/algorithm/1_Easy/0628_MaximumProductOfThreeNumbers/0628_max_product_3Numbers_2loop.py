from typing import List
import sys
import time

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        max_prod = -sys.maxsize-1
        for x in range(len(nums)-2):
            left, right, prod = x+1, len(nums)-1, 1
            while left < right:
                prod = 1
                prod *= nums[x] * nums[left] * nums[right]
                max_prod = max(max_prod, prod)
                if prod < max_prod:
                    left += 1
                else:
                    right -= 1
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


