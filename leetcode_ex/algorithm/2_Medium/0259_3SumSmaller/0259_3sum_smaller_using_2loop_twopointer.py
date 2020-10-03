from typing import List
import collections
import time

class Solution:
    def threeSumSmaller(self, nums: List[int], K: int) -> int:
        def twoSumSmaller(nums: List[int], start: int, target: int) -> int:
            count, left, right = 0, start, len(nums)-1
            while left < right:
                if nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count

        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            count += twoSumSmaller(nums, i+1, K-nums[i])
        return count


def main():
    sol = Solution()
    inputs = [[-2,0,1,3], [], [0], [1,1,-2], [3,1,0,-2]]
    Ks = [2, 0, 0, 1, 4]
    outputs = [2, 0, 0, 1, 3]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.threeSumSmaller(inputs[i], Ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


