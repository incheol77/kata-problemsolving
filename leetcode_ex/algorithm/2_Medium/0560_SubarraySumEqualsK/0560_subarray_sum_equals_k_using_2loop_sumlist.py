from typing import List
import collections
import sys
import time

class Solution:
    def subarraySum(self, A: List[int], K: int) -> int:
        count = 0
        sums = [0] * (len(A)+1)
        sums[0] = 0
        for i in range(1, len(A)+1):
            sums[i] = sums[i-1] + A[i-1]
        for start in range(len(A)):
            for end in range(start+1, len(A)+1):
                if sums[end] - sums[start] == K:
                    count += 1
        return count


def main():
    sol = Solution()
    inputs = [[1,1,1], [1,2,3]]
    Ks = [2, 3]
    outputs = [2, 2]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.subarraySum(inputs[i], Ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()


