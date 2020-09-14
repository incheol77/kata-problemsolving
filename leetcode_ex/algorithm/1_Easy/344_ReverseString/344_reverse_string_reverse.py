from typing import List
import time


class Solution:
    def reverse_string(self, s: List[str]) -> None:
		    s.reverse()


def main():
    sol = Solution()
    strs = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"]]
    reversed_strs = [["o","l","l","e","h"], ["h","a","n","n","a","H"]]
    for i in range(len(strs)):
        print(strs[i])
        start = time.time()
        sol.reverse_string(strs[i])
        end = time.time()
        print(reversed_strs[i])
        print(end-start, " sec")
        if strs[i] != reversed_strs[i]:
            print(False)
    print(True)


if __name__ == "__main__":
    main()

