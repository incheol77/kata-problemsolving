from typing import List
import sys
import time

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = -sys.maxsize-1
        for start in range(len(nums)):
            for end in range(len(nums)+1):
                sub_max = 0
                for i in range(start, end):
                    sub_max += nums[i]
                    max_sum = max(max_sum, sub_max)
        return max_sum


def main():
    sol = Solution()
    inputs = [[-2,1,-3,4,-1,2,1,-5,4], [1], [0], [-1], [-2147483647], [-2,1]]
    outputs = [6, 1, 0, -1, -2147483647, 1]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maxSubArray(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


