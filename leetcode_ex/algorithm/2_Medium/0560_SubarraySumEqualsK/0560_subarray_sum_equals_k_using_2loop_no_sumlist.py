from typing import List
import collections
import sys
import time

class Solution:
    def subarraySum(self, A: List[int], K: int) -> int:
        count = 0
        for start in range(len(A)):
            sum = 0
            for end in range(start, len(A)):
                sum += A[end]
                if sum == K:
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


