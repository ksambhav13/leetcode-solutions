# [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
import heapq


class MedianFinder:
    def __init__(self):
        self.lheap = []
        self.rheap = []

    def addNum(self, num: int) -> None:
        if len(self.lheap) == len(self.rheap):
            heapq.heappush(self.rheap, num)
            item = heapq.heappop(self.rheap)
            heapq.heappush(self.lheap, -item)
        else:
            heapq.heappush(self.lheap, -num)
            item = -heapq.heappop(self.lheap)
            heapq.heappush(self.rheap, item)

    def findMedian(self) -> float:
        if len(self.lheap) == len(self.rheap):
            return (-self.lheap[0] + self.rheap[0]) / 2
        else:
            return -self.lheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
testcases = [
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
    [[], [1], [2], [], [3], []],
]

for i in range(0, len(testcases), 2):
    obj = globals()[testcases[i][0]](*testcases[i + 1][0])
    print(None)
    for j in range(1, len(testcases[i])):
        method = getattr(obj, testcases[i][j])
        print(method(*testcases[i + 1][j]))
