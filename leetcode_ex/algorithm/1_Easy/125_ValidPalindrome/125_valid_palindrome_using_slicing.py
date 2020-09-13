import time
import re


class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


def main():
    sol = Solution()
    input_str = ["A man, a plan, a canal: Panama", "race a car"]
    for s in input_str:
        start = time.time()
        res = sol.is_palindrome(s)
        end = time.time()
        print(res, " : ", end-start, " sec")


if __name__ == "__main__":
    main()

