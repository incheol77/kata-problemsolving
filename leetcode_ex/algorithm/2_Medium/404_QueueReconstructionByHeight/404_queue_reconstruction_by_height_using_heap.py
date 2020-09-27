from typing import List
import heapq
import time

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result


def main():
    sol = Solution()
    inputs = [[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]]
    outputs = [[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.reconstructQueue(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()

