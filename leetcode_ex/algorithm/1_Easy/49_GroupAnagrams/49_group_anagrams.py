import collections
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


def main():
    inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    outputs = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    sol = Solution()
    if outputs == sol.group_anagrams(inputs):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()

