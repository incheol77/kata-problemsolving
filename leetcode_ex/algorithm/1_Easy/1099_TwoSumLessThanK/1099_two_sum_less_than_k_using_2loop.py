from typing import List
import sys
import time

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_sum = -1
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < K:
                    max_sum = max(max_sum, A[i] + A[j])

        return max_sum


def main():
    sol = Solution()
    inputs = [[34,23,1,24,75,33,54,8], [10,20,30]]
    Ks = [60, 15]
    outputs = [58, -1]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.twoSumLessThanK(inputs[i], Ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


