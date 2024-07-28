# [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False

        half = sum_num // 2

        dp = set()
        dp.add(0)
        for num in nums:
            next_dp = dp.copy()
            for ssum in dp:
                if ssum + num == half:
                    return True
                elif ssum + num < half:
                    next_dp.add(ssum + num)
            dp = next_dp
        return False


testcases = [
    [1, 5, 11, 5],
    [1, 2, 3, 5],
]


for testcase in testcases:
    print(Solution().canPartition(testcase))
