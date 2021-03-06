from typing import List
import sys
import time

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        max_windows = []
        for i in range(len(nums)-k+1):
            max_windows.append(max(nums[i:i+k]))
        return max_windows


def main():
    sol = Solution()
    inputs = [[1,3,-1,-3,5,3,6,7], [1], [1,-1], [9,11], [4,-2]]
    ks = [3, 1, 1, 2, 2]
    outputs = [[3,3,5,5,6,7], [1], [1,-1], [11], [4]]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maxSlidingWindow(inputs[i], ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()

