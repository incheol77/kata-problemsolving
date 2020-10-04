from typing import List
import sys
import time

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[len(nums)-1],                 
                   nums[len(nums)-1] * nums[len(nums)-2] * nums[len(nums)-3])


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


