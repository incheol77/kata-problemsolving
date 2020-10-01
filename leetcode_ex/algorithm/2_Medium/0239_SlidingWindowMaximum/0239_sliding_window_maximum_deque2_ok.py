from typing import List
import collections
import time

class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        queue = []
        for i, v in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue = queue[1:]
            while queue and nums[queue[-1]] < v:
                queue.pop()
            queue.append(i)
            if i + 1 >= k:
                ans.append(nums[queue[0]])
        return ans


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

