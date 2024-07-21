# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        li, r = 0, len(A) - 1

        while True:
            i = (li + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                li = i + 1

    def findMedianSortedArraysWithMerge(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        is_even = (m + n) % 2 == 0

        def get_min():
            nonlocal p1, p2
            if p1 == m:
                ans = nums2[p2]
                p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        for _ in range((m + n) // 2 - 1):
            _ = get_min()
        if is_even:
            return (get_min() + get_min()) / 2
        else:
            _ = get_min() if (m + n) > 1 else None
            return get_min()


testcases = [
    [1, 3],
    [2],
    [1, 2],
    [3, 4],
]

for i in range(0, len(testcases), 2):
    print(Solution().findMedianSortedArrays(testcases[i], testcases[i + 1]))
