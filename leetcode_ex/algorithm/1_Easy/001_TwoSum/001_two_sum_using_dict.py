import time
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target-n]:
                return [nums.index(n), nums_map[target-n]]


def main():
    count = 3
    inputs = [[2,7,11,15], [3,2,4], [3,3]]
    targets = [9, 6, 6]
    outputs = [[0,1], [1,2], [0,1]]

    sol = Solution()
    for i in range(count):
        start = time.time()
        res = sol.two_sum(inputs[i], targets[i])
        end = time.time()
        if outputs[i] == res:
            print(True, " : ", end-start, " sec")
        else:
            print(False, " : ", end-start, " sec")


if __name__ == "__main__":
    main()
