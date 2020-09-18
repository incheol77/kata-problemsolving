import time
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


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
