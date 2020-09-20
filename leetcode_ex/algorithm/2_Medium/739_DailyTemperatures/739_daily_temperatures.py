import time
from typing import List

class Solution:
    def daily_temperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            #print(cur, i, answer, stack)
        return answer


def main():
    sol = Solution()
    inputs = [73, 74, 75, 71, 69, 72, 76, 73]
    outputs = [1, 1, 4, 2, 1, 1, 0, 0]

    start = time.time()
    res = sol.daily_temperatures(inputs)
    end = time.time()
    if res == outputs:
        print("true : ", end-start, " sec")
    else:
        print("false : ", end - start, " sec")


if __name__ == "__main__":
    main()
