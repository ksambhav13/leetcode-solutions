# [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_account:
                    uf.union(i, email_account[email])
                else:
                    email_account[email] = i
        email_group = defaultdict(list)
        for email, i in email_account.items():
            leader = uf.find(i)
            email_group[leader].append(email)

        res = []
        for i, emails in email_group.items():
            t = [accounts[i][0]] + sorted(emails)
            res.append(t)

        return res


testcases = [
    [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ],
    [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
    ],
]

for testcase in testcases:
    print(Solution().accountsMerge(testcase))
