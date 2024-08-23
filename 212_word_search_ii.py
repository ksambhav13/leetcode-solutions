# [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.complete = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        dirs = [0, 1, 0, -1, 0]

        root = TrieNode()
        for word in words:
            root.insert(word)
        res = set()
        path = set()

        def dfs(i, j, node, word):
            if (
                i < 0
                or i >= m
                or j < 0
                or j >= n
                or (i, j) in path
                or board[i][j] not in node.children
            ):
                return False

            path.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.complete:
                res.add(word)
            for k in range(4):
                dfs(i + dirs[k], j + dirs[k + 1], node, word)

            path.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)


testcases = [
    [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    ["oath", "pea", "eat", "rain"],
    [["a", "b"], ["c", "d"]],
    ["abcb"],
]


for i in range(0, len(testcases), 2):
    print(Solution().findWords(testcases[i], testcases[i + 1]))
