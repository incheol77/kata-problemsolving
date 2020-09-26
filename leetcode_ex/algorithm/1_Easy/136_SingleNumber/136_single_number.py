import collections
import heapq
import time
from typing import List

class Solution:
    def single_number(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


def main():
    sol = Solution()
    inputs = [[2,2,1], [4,1,2,1,2]]
    outputs = [1, 4]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.single_number(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()
