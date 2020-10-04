from typing import List
import time

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = max_prod = min_prod = nums[0]
        for n in nums[1:]:
            max_prod, min_prod = max(n, max_prod * n, min_prod * n), min(n, max_prod * n, min_prod * n)
            result = max(result, max_prod)
        return result


def main():
    sol = Solution()
    inputs = [[2,3,-2,4], [-2,0,-1], [0,2]]
    outputs = [6, 0, 2]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.maxProduct(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


