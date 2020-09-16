class Solution:
    def longest_palindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


def main():
    inputs = ["babad", "cbbd"]
    outputs = ["bab", "bb"]
    sol = Solution()
    for i in range(len(inputs)):
        if outputs[i] == sol.longest_palindrome(inputs[i]):
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()

