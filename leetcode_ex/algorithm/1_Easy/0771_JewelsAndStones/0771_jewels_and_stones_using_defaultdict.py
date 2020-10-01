import collections
import time

class Solution:
    def num_jewels_in_stone(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        for char in S:
            freqs[char] += 1
        for char in J:
            count += freqs[char]
        return count


def main():
    sol = Solution()
    input_j = ["aA","z"]
    input_s = ["aAAbbbb", "ZZ"]
    outputs = [3, 0]

    for i in range(len(input_j)):
        start = time.time()
        res = sol.num_jewels_in_stone(input_j[i], input_s[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")



if __name__ == "__main__":
    main()
