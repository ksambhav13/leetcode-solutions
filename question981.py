# [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)


class TimeMap:
    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = [[timestamp, value]]
        else:
            self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        tvalues = self.values.get(key, [])
        l, r = 0, len(tvalues) - 1
        res = ""
        iter = 0
        while r >= l:
            iter += 1
            mid = (l + r) // 2
            if tvalues[mid][0] <= timestamp:
                res = tvalues[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.get("foo", 1)
