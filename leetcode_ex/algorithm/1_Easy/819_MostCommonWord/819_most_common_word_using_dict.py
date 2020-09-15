import collections
from typing import List
import re


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
            .lower().split() if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        print(counts)
        return max(counts, key=counts.get)


def main():
    sol = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    output = "ball"
    if output == sol.most_common_word(paragraph, banned):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()

