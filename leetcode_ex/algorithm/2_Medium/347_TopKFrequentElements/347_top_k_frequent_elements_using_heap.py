import collections
import heapq
from typing import List
import time

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk


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

