import collections
import time

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index-start+1)
            used[char] = index
        return max_length


def main():
    sol = Solution()
    inputs = ["abcabcbb", "bbbbb", "pwwkew"]
    outputs = [3, 1, 3]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.length_of_longest_substring(inputs[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()
