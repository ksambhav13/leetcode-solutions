# [46. Permutations](https://leetcode.com/problems/permutations/)

from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rec = []
        n = len(nums)

        def permute_rec(nums, ci):
            print(f"{nums=}, {ci=}")
            print(f"{ci=}")
            if ci == n - 1:
                rec.append(nums.copy())
                return
            for index in range(ci, n):
                nums[ci], nums[index] = nums[index], nums[ci]
                permute_rec(nums, ci + 1)
                nums[ci], nums[index] = nums[index], nums[ci]

        permute_rec(nums, 0)
        return rec

    def permuteBFS(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        q = deque()
        res = []
        q.append([])
        while q:
            perm = q.popleft()
            if len(perm) == n:
                res.append(perm)
            else:
                for num in nums:
                    if num not in perm:
                        q.append(perm + [num])
        return res


testcases = [
    [1, 2, 3],
    [0, 1],
    [1],
]

for testcase in testcases:
    print(Solution().permute(testcase))
