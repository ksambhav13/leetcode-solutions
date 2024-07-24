# [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)


class Node:
    def __init__(self, val: str, complete: bool = False, children: dict = None):
        self.val = val
        self.complete = complete
        self.children = children if children else {}

    def __repr__(self) -> str:
        return f"val = {self.val}, complete = {self.complete}"


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        prev = self.root
        split = ""
        for ch in word:
            split = split + ch
            cur = None
            if split in prev.children:
                cur = prev.children[split]
            else:
                cur = Node(split)
                prev.children[split] = cur
            prev = cur
        prev.complete = True

    def search(self, word: str) -> bool:
        prev = self.root
        split = ""
        for ch in word:
            split = split + ch
            if split not in prev.children:
                return False
            prev = prev.children[split]
        # print(prev)
        return prev.complete

    def startsWith(self, prefix: str) -> bool:
        prev = self.root
        split = ""
        for ch in prefix:
            split = split + ch
            if split not in prev.children:
                return False
            prev = prev.children[split]
        return True


obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))

# print(obj.search("t"))

# print("---------")
# obj = Trie()
# print(obj.search("a"))
