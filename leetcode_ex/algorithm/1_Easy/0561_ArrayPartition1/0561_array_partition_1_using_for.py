import time
from typing import List


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum


def main():
    inputs = [1, 4, 3, 2]
    output = 4
    sol = Solution()
    start_time = time.time()
    res = sol.array_pair_sum(inputs)
    end_time = time.time()
    if res == output:
        print(True, " : ", end_time - start_time, " sec")
    else:
        print(False, " : ", end_time - start_time, " sec")


if __name__ == "__main__":
    main()

