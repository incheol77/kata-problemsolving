import time
from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i]
#            print(nums[i], p, res[i])
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            res[i] = res[i] * p
            p = p * nums[i]
#            print(nums[i], p, res[i])
        return res


def main():
    inputs = [1,2,3,4]
    outputs = [24,12,8,6]
    sol = Solution()
    start = time.time()
    res = sol.product_except_self(inputs)
    end = time.time()
    if res == outputs:
        print(True, " : ", end-start, " sec")
    else:
        print(False, " : ", end-start, " sec")


if __name__ == "__main__":
    main()



