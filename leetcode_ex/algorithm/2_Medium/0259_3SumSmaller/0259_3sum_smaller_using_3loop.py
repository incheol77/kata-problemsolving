from typing import List
import collections
import time

class Solution:
    def threeSumSmaller(self, nums: List[int], K: int) -> int:
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for m in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[m] < K:
                        res.append([nums[i], nums[j], nums[m]])
        print(res)
        return len(res)


def main():
    sol = Solution()
    inputs = [[-2,0,1,3], [], [0]]
    Ks = [2, 0, 0]
    outputs = [2, 0, 0]

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


