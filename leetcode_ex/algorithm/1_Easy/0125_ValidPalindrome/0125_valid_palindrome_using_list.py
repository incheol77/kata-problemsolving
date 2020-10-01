import time


class Solution:
    def is_palindrome(self, s: str) -> bool:
        # preprocessing for string (convert to list)
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())

        # determine whether palindrome or not
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True


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

