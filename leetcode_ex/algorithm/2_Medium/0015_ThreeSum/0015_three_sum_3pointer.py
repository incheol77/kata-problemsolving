import time
from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res


def main():
    inputs = [[-1,0,1,2,-1,-4], [], [0]]
    outputs = [[[-1,-1,2],[-1,0,1]], [], []]
    sol = Solution()
    for i in range(len(inputs)):
        start = time.time()
        res = sol.three_sum(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print(True, " : ", end - start, " sec")
        else:
            print(False, " : ", end - start, " sec")


if __name__ == "__main__":
    main()




