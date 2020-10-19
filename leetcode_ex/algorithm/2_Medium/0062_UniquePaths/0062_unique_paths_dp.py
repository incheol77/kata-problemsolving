import time

class Solution:
    def uniquePath(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for col in range (1, m):
            for row in range(1, n):
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        return dp[m-1][n-1]


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
