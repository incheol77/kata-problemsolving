import collections
from typing import List
import time

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = sorted(collections.Counter(nums).items(), key=(lambda x: x[1]), reverse=True)
        res = []
        count = 0
        for key, val in freqs:
            if count < k:
                res.append(key)
                count += 1
            else:
                break
        return res


def main():
    sol = Solution()
    inputs = [[1,1,1,2,2,3], [1], [1,1,3,3,3,3], [3,0,1,0]]
    ks = [2, 1, 2, 1]
    outputs = [[1,2], [1], [3,1], [0]]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.topKFrequent(inputs[i], ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()

