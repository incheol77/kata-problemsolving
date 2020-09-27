from typing import List
import collections
import time

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            result.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return result


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

