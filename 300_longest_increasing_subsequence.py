# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [0] * n
        i = n - 1
        while i >= 0:
            maxi = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    maxi = max(maxi, 1 + lis[j])
            lis[i] = maxi
            i -= 1
        return max(lis)


testcases = [
    [10, 9, 2, 5, 3, 7, 101, 18],
    [0, 1, 0, 3, 2, 3],
    [7, 7, 7, 7, 7, 7, 7],
]


for testcase in testcases:
    print(Solution().lengthOfLIS(testcase))
