import time
from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
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




