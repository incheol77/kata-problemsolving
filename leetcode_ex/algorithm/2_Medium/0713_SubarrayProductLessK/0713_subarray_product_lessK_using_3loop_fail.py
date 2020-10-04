from typing import List
import collections
import time

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], K: int) -> int:
        nums.sort()
        #print(nums)
        res = []
        for start in range(len(nums)):
            if nums[start] >= K or (start > 0 and nums[start-1] == nums[start]):
                continue
            for end in range(start, len(nums)+1):
                #if end > start and nums[end-1] == nums[end]:
                #    continue
                prod = 1
                prod_elems = []
                for i in range(start, end):
                    if i > start + 1 and nums[i-1] == nums[i]:
                        continue
                    prod *= nums[i]
                    prod_elems.append(nums[i])
                if prod >= K:
                    continue
                if prod != 1:
                    res.append(prod_elems)
        #print(res)
        #print(len(res))
        return len(res)


def main():
    sol = Solution()
    #inputs = [[10, 5, 2, 6], [10,9,10,4,3,8,3,3,6,2,10,10,9,3]]
    #Ks = [100, 19]
    inputs = [[10, 5, 2, 6], [10,9,10,4,3,8,3,3,6,2,10,10,9,3]]
    Ks = [100, 19]
    outputs = [8, 18]

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


