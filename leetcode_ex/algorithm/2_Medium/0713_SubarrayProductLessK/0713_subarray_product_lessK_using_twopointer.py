from typing import List
import collections
import time

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count, left, prod = 0, 0, 1
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count


def main():
    sol = Solution()
    #inputs = [[10, 5, 2, 6], [10,9,10,4,3,8,3,3,6,2,10,10,9,3]]
    #Ks = [100, 19]
    inputs = [[10, 5, 2, 6], [10,9,10,4,3,8,3,3,6,2,10,10,9,3], [1,1,1], [1,2,3]]
    Ks = [100, 19, 2, 0]
    outputs = [8, 18, 6, 0]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.numSubarrayProductLessThanK(inputs[i], Ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


