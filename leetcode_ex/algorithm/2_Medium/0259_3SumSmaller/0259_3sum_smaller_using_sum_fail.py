from typing import List
import collections
import time

class Solution:
    def threeSumSmaller(self, nums: List[int], K: int) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3 and (nums[0] + nums[1] + nums[2] < K):
            return 1

        count = 0
        sums = [0] * (len(nums) + 1)
        sums[0] = 0
        nums.sort()
        for i, n in enumerate(nums):
            sums[i+1] = sums[i] + n

        for start in range(1, len(sums)-3):
            for end in range(start+1, start+4):
                if sums[end] - sums[start] < K:
                    count += 1
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


