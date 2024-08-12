# [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)


from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = defaultdict(lambda: [0, ""])
        for i in words:
            cnt[i] = [cnt[i][0] - 1, i]
        lst = list(cnt.values())
        heapq.heapify(lst)
        print(lst)
        lst = heapq.nsmallest(k, lst)
        ans = []
        for i in lst:
            ans.append(i[1])
        return ans

    def topKFrequentMine(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        heap = []
        for word, count in word_count.items():
            if len(heap) < k:
                heapq.heappush(heap, [count, word])
            else:
                heapq.heappushpop(heap, [count, word])

        return [heapq.heappop(heap)[1] for _ in range(k)]


testcases = [
    ["love", "i", "leetcode", "i", "love", "coding"],
    2,
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
    4,
]


for i in range(0, len(testcases), 2):
    print(Solution().topKFrequentMine(testcases[i], testcases[i + 1]))
