import time

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


def main():
    sol = Solution()
    inputs = ["()", "()[]{}", "(]"]
    outputs = [True, True, False]

    for i, s in enumerate(inputs):
        start = time.time()
        res = sol.is_valid(s)
        end = time.time()
        if res == outputs[i]:
            print("true")
        else:
            print("false")
        print(end-start, " sec")


if __name__ == "__main__":
    main()
