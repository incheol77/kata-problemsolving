import time

class Solution:
    def uniquePath(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePath(m-1, n) + self.uniquePath(m, n-1)


def main():
    sol = Solution()
    inputs = [[3,7], [3,2], [7,3], [3,3], [23,12]]
    outputs = [28, 3, 28, 6, 193536720]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.uniquePath(inputs[i][0], inputs[i][1])
        end = time.time()
        if res == outputs[i]:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()
