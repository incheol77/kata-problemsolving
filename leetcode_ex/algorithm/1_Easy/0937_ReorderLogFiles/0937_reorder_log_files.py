from typing import List
import time


class Solution:
    def reorder_log_files(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits


def main():
    sol = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    ans = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    start = time.time()
    reordered_logs = sol.reorder_log_files(logs)
    end = time.time()
    res = True if reordered_logs == ans else False
    print(reordered_logs)
    print(res, ":", end-start, " sec")


if __name__ == "__main__":
    main()

