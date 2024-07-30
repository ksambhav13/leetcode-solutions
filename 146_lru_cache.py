# [146. LRU Cache](https://leetcode.com/problems/lru-cache/)


class DoublyListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"val = {self.val}"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, DoublyListNode] = {}
        self.left: DoublyListNode = DoublyListNode(-1, -1)
        self.right: DoublyListNode = DoublyListNode(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

        self.size: int = 0

    def remove(self, v):
        v.prev.next = v.next
        v.next.prev = v.prev

    def insert_left(self, v):
        v.prev = self.left
        v.next = self.left.next
        self.left.next.prev = v
        self.left.next = v

    def get(self, key: int) -> int:
        v = self.cache.get(key)
        if not v:
            return -1
        if self.left.next != v:
            self.remove(v)
            self.insert_left(v)
        return v.val

    def put(self, key: int, value: int) -> None:
        v = self.cache.get(key)
        if v:
            v.val = value
            if self.left.next != v:
                self.remove(v)
                self.insert_left(v)
            return

        v = DoublyListNode(key, value)
        self.size += 1
        self.cache[key] = v
        self.insert_left(v)

        if self.size > self.capacity:
            # evict key
            self.cache.pop(self.right.prev.key)
            self.remove(self.right.prev)
            self.size -= 1

        # print(f"PUT: {self.left.next=}, {self.right.prev=}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


testcases = [
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
]

for i in range(0, len(testcases), 2):
    obj = globals()[testcases[i][0]](*testcases[i + 1][0])
    print(None)
    for j in range(1, len(testcases[i])):
        method = getattr(obj, testcases[i][j])
        print(method(*testcases[i + 1][j]))
