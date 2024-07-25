# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[r]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

        def bs(i, j):
            if i > j or i < 0 or j >= len(nums):
                return -1

            left = target >= nums[0]
            mleft = nums[mid] >= nums[0]
            if left == mleft:
                if target > nums[mid]:
                    return bs(mid + 1, j)
                else:
                    return bs(i, mid - 1)
            elif mleft:
                return bs(mid + 1, j)
            else:
                return bs(i, mid - 1)

        return bs(0, len(nums) - 1)


testcases = [
    # [4, 5, 6, 7, 0, 1, 2],
    # 0,
    # [4, 5, 6, 7, 0, 1, 2, 3],
    # 3,
    # [1],
    # 0,
    [1, 3],
    3,
]

for i in range(0, len(testcases), 2):
    print(Solution().search(testcases[i], testcases[i + 1]))
