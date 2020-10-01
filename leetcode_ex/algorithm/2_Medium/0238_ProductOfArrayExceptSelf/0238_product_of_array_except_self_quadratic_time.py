import time
from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            prod = 1
            for j, m in enumerate(nums):
                if i != j:
                    prod *= m
            res.append(prod)
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



