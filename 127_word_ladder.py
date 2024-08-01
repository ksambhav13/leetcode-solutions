# [127. Word Ladder](https://leetcode.com/problems/word-ladder/)


from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                adj[pattern].append(word)

        visited = set([beginWord])
        q = deque()
        res = 1
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for adj_word in adj[pattern]:
                        if adj_word not in visited:
                            visited.add(adj_word)
                            q.append(adj_word)
            res += 1

        return 0


testcases = [
    "hit",
    "cog",
    ["hot", "dot", "dog", "lot", "log", "cog"],
    "hit",
    "cog",
    ["hot", "dot", "dog", "lot", "log"],
]


for i in range(0, len(testcases), 3):
    print(Solution().ladderLength(testcases[i], testcases[i + 1], testcases[i + 2]))
