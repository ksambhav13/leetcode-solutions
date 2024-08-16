# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)


from typing import List

[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6, 7, 8, 9]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        if m > n:
            nums1, nums2 = nums2, nums1
        l, r = 0, m - 1
        while True:
            am = (l + r) // 2
            aleft = nums1[am] if am >= 0 else float("-infinity")
            aright = nums1[am + 1] if am + 1 < m else float("infinity")

            bm = mid - (am + 1) - 1
            print(f"{am=}, {bm=}")
            bleft = nums2[bm] if bm >= 0 else float("-infinity")
            bright = nums2[bm + 1] if bm + 1 < n else float("infinity")
            if aleft <= bright and bleft <= aright:
                break
            elif aleft > bright:
                r = am - 1
            else:
                l = am + 1
        print(f"{aleft=}, {aright=}, {bleft=}, {bright=}")
        if (m + n) % 2 == 0:
            return (max(aleft, bleft) + min(aright, bright)) / 2
        else:
            return min(aright, bright)

    def findMedianSortedArraysMerge(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        prev, cur = 0, 0
        while i + j <= mid:
            if i >= m:
                prev = cur
                cur = nums2[j]
                j += 1
            elif j >= n:
                prev = cur
                cur = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                prev = cur
                cur = nums1[i]
                i += 1
            else:
                prev = cur
                cur = nums2[j]
                j += 1
        print(f"{prev=}, {cur=}, {i=}, {j=}")
        if (m + n) % 2 == 1:
            return cur
        else:
            return (prev + cur) / 2


testcases = [
    [1, 3],
    [2],
    [1, 2],
    [3, 4],
    [5, 6],
    [1, 2, 3, 4],
]


for i in range(0, len(testcases), 2):
    print(Solution().findMedianSortedArrays(testcases[i], testcases[i + 1]))
