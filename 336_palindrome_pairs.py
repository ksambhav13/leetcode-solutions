# [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)


from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palin(w, s, e):
            while s < e:
                if w[s] != w[e]:
                    return False
                s += 1
                e -= 1
            return True

        res = []
        lookup = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            if word == "":
                for j in range(len(words)):
                    if j != i and words[j] in lookup and lookup[words[j]] == j:
                        res.append([i, j])
                        res.append([j, i])
                continue

            if word in lookup and lookup[word] != i:
                res.append([i, lookup[word]])

            for k in range(1, len(word)):
                if word[k:] in lookup and is_palin(word, 0, k - 1):
                    res.append([lookup[word[k:]], i])

                if word[:k] in lookup and is_palin(word, k, len(word) - 1):
                    res.append([i, lookup[word[:k]]])
        return res


testcases = [
    ["abcd", "dcba", "lls", "s", "sssll", ""],
    ["bat", "tab", "cat"],
    ["a", ""],
]


for testcase in testcases:
    print(Solution().palindromePairs(testcase))
