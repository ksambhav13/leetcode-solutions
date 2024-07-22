class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        bad = 0
        while l <= r:
            mid = (l + r) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                bad = mid
                r = mid - 1
            else:
                l = mid + 1

        return bad

    def firstBadVersionRecursive(self, n: int) -> int:
        def bs(i, j):
            if i >= j:
                return i
            mid = (i + j) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                return bs(i, mid)
            else:
                return bs(mid + 1, j)

        return bs(1, n)


def isBadVersion(version: int) -> bool:
    return version >= bad_version


testcases = [5, 4, 1, 1]
bad_version = 0
for i in range(0, len(testcases), 2):
    bad_version = testcases[i + 1]
    print(Solution().firstBadVersion(testcases[i]))
